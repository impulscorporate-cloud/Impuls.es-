# -*- coding: utf-8 -*-
"""
Impuls Longevity — generador de sitio estático (ES / RU / EN).
Ejecutar:  python3 build.py
Lee content.py + services.py y escribe HTML limpio en la carpeta del sitio.
"""
import os, html, json, re
from content import LANGS, HOME, UI, CONTACT, BRANDS, HOME_CONTENT, COMPANY, REVIEWS, REVIEW_UI
from services import SERVICES
from pages import ABOUT, CONTACTP
from legal import LEGAL, PROMO, UPDATED, TRANS_NOTE
from blog import BLOG_INDEX, BLOG_POSTS
from privacy import PRIVACY_POLICY

# Política de privacidad completa (transferida del sitio original) sustituye la versión resumida
LEGAL["politica-de-privacidad"] = PRIVACY_POLICY

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://impuls.es"
GTM = "GTM-M2GNTDX"
PIXEL = "1040600500573477"
# amoCRM: envío directo al endpoint de formularios web (mismo método que adelgazarnatural.es).
# form_id + hash identifican la форма-web de amoCRM (embudo/etapa destino). Los IDs de campo
# (949379 tel, 949381 email) son de cuenta → los mismos que en adelgazar (misma cuenta amoCRM).
AMO_ENDPOINT = "https://forms.amocrm.ru/queue/add"
AMO_FORM_ID = "1735274"                                # форма «Impuls.es (new site)» → Sucursal Barcelona / Interesado
AMO_HASH = "ca114f35e3ae13305a69acd227ebad86"
# Prefijos de país para el teléfono (como en adelgazarnatural). El primero es el por defecto.
PHONE_CODES = [
    ("+34", "🇪🇸 +34"), ("+7", "🇷🇺 +7"), ("+380", "🇺🇦 +380"), ("+44", "🇬🇧 +44"),
    ("+33", "🇫🇷 +33"), ("+49", "🇩🇪 +49"), ("+39", "🇮🇹 +39"), ("+351", "🇵🇹 +351"),
    ("+31", "🇳🇱 +31"), ("+32", "🇧🇪 +32"), ("+41", "🇨🇭 +41"), ("+46", "🇸🇪 +46"),
    ("+1", "🇺🇸 +1"), ("+212", "🇲🇦 +212"), ("+971", "🇦🇪 +971"), ("+40", "🇷🇴 +40"),
    ("+48", "🇵🇱 +48"),
]

def esc(s): return html.escape(s, quote=True)

# ---------- Datos estructurados (schema.org) para SEO local ----------
_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "MedicalClinic",
    "name": "Impuls Longevity",
    "legalName": COMPANY["razon_social"],
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/assets/longevity-logo.svg",
    "image": DOMAIN + "/assets/og.jpg",
    "telephone": CONTACT["phones_tel"][0],
    "email": COMPANY["email"],
    "priceRange": "€€",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Plaza Urquinaona 6, Planta 14, Puerta A1",
        "addressLocality": "Barcelona",
        "postalCode": "08010",
        "addressCountry": "ES",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 41.3907, "longitude": 2.1699},
    "areaServed": {"@type": "City", "name": "Barcelona"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "20:30"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:30", "closes": "18:00"},
    ],
    "sameAs": [CONTACT["instagram"], CONTACT["facebook"]],
    "medicalSpecialty": "Dermatology",
    "availableService": [
        "Depilación láser", "Aclaración de tatuajes con láser", "Rejuvenecimiento facial láser",
        "Aclaración de manchas", "Tratamiento de rosácea y arañas vasculares",
        "Tratamiento del acné", "Cicatrices y estrías", "Láser Fotona 4D",
    ],
}
JSONLD = '<script type="application/ld+json">' + json.dumps(_SCHEMA, ensure_ascii=False) + '</script>'


def faq_jsonld(faq):
    """FAQPage (schema.org) desde una lista de (pregunta, respuesta).
    Hace que buscadores de IA (ChatGPT, Google AI) y Google extraigan las Q&A."""
    if not faq:
        return ""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }
    return '\n<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'

# ---------- Cabezas / analítica ----------
def head(lang, title, desc, canonical, alts, faq=None):
    hreflang = "\n".join(
        f'<link rel="alternate" hreflang="{hl}" href="{DOMAIN}{u}" />' for hl, u in alts.items()
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{DOMAIN}{alts["es"]}" />'
    return f'''<!DOCTYPE html>
<html lang="{UI[lang]["html_lang"]}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}" />
<link rel="canonical" href="{DOMAIN}{canonical}" />
{hreflang}
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:image" content="{DOMAIN}/assets/og.jpg" />
<meta property="og:url" content="{DOMAIN}{canonical}" />
<meta property="og:type" content="website" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/styles.css" />
{JSONLD}{faq_jsonld(faq)}
<script>
(function(){{
  window.__impulsLoadAnalytics=function(){{
    (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM}');
    !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{PIXEL}');fbq('track','PageView');
  }};
  try{{if(localStorage.getItem('impuls_consent')==='accepted'){{window.__impulsLoadAnalytics();}}}}catch(e){{}}
}})();
</script>
</head>
<body>
<a class="skip" href="#main">{esc(UI[lang]["skip"])}</a>
'''

# ---------- Cabecera / navegación ----------
def header(lang, alts):
    m = UI[lang]["menu"]; home = HOME[lang]
    langlinks = ""
    for L in LANGS:
        cls = ' class="is-active"' if L == lang else ""
        langlinks += f'<a{cls} href="{alts[L]}">{L.upper()}</a>'
    return f'''<header class="site-header">
  <nav class="nav container" data-open="false">
    <a class="nav__logo" href="{home}" aria-label="Impuls Longevity">
      <img src="/assets/longevity-logo.svg" alt="Impuls Longevity" />
    </a>
    <ul class="nav__menu">
      <li><a href="{home}#servicios">{esc(m["servicios"])}</a></li>
      <li><a href="{home}programas/">{esc(m["programas"])}</a></li>
      <li><a href="{home}sobre-nosotros/">{esc(m["sobre"])}</a></li>
      <li><a href="{home}contacto/">{esc(m["contacto"])}</a></li>
    </ul>
    <div class="nav__right">
      <div class="lang" aria-label="Idioma">{langlinks}</div>
      <a class="nav__tel" href="tel:{CONTACT["phones_tel"][0]}" aria-label="{esc(_CALL_LABEL[lang])} {CONTACT["phones"][0]}">{_TEL_SVG}</a>
      <a class="btn btn-primary" href="#cita">{esc(UI[lang]["cta_nav"])}</a>
      <button class="nav__toggle" aria-label="Menu" onclick="var n=this.closest('.nav');n.dataset.open=n.dataset.open==='true'?'false':'true'">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </nav>
</header>
<main id="main">
'''

# ---------- Formulario / CTA ----------
def cta_form(lang, page_id):
    u = UI[lang]; f = u["form"]; home = HOME[lang]
    consent = f["consent"].format(url=f"{home}politica-de-privacidad/")
    return f'''<section class="section" id="cita">
  <div class="container">
    <div class="cta">
      <div>
        <span class="eyebrow">{esc(u["cta_nav"])}</span>
        <h2>{esc(u["service_cta_h"])}</h2>
        <p>{esc(u["service_cta_p"])}</p>
      </div>
      <form class="form" id="lead-form" method="POST" action="#" data-endpoint="" onsubmit="return impulsSubmit(this)">
        <label class="form__field"><span class="sr-only">{esc(f["nombre"])}</span>
          <input type="text" name="nombre" placeholder="{esc(f["nombre"])} *" aria-label="{esc(f["nombre"])}" required /></label>
        <label class="form__field"><span class="sr-only">{esc(f["telefono"])}</span>
          <div class="phone-row">
            <select name="phone_code" class="phone-code" aria-label="{esc(f.get("phone_code", "Código de país"))}">{"".join(f'<option value="{v}"{" selected" if i==0 else ""}>{t}</option>' for i,(v,t) in enumerate(PHONE_CODES))}</select>
            <input type="tel" name="telefono" placeholder="{esc(f["telefono"])} *" aria-label="{esc(f["telefono"])}" required />
          </div></label>
        <label class="form__field"><span class="sr-only">{esc(f["email"])}</span>
          <input type="email" name="email" placeholder="{esc(f["email"])}" aria-label="{esc(f["email"])}" /></label>
        <label class="form__field"><span class="sr-only">{esc(f["mensaje"])}</span>
          <textarea name="mensaje" rows="3" placeholder="{esc(f["mensaje"])}" aria-label="{esc(f["mensaje"])}"></textarea></label>
        <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" />
        <input type="hidden" name="idioma" value="{lang}" />
        <input type="hidden" name="pagina" value="{esc(page_id)}" />
        <label class="form__check"><input type="checkbox" name="privacidad" required /> <span>{consent}</span></label>
        <button type="submit" class="btn btn-primary">{esc(f["enviar"])}</button>
        <div class="form__success" role="status">{esc(f["success"])}</div>
      </form>
    </div>
  </div>
</section>
'''

# ---------- Pie ----------
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15l-1.3 4.6 4.7-1.2A10 10 0 1012 2zm5.5 14.2c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .2-3.2-.7-2.7-1.1-4.4-3.9-4.5-4-.1-.2-1-1.4-1-2.6s.6-1.8.9-2c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6c-.2.2-.3.4-.1.7.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.7-.9c.2-.2.4-.2.6-.1l2 .9c.2.1.4.2.4.3.1.2.1.9-.1 1.4z"/></svg>'

def footer(lang):
    u = UI[lang]; home = HOME[lang]
    # 4 servicios destacados
    feat = SERVICES[:4]
    serv_links = "".join(f'<li><a href="{home}{s["slug"]}/">{esc(s[lang]["name"])}</a></li>' for s in feat)
    legal = " · ".join(f'<a href="{home}{slug}/">{esc(label)}</a>' for label, slug in u["legal_links"])
    legal_lis = "".join(f'<li><a href="{home}{slug}/">{esc(label)}</a></li>' for label, slug in u["legal_links"])
    phones = "".join(f'<li><a href="tel:{t}">{esc(p)}</a></li>' for p, t in zip(CONTACT["phones"], CONTACT["phones_tel"]))
    return f'''</main>
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="/assets/longevity-logo-white.svg" alt="Impuls Longevity" loading="lazy" />
        <p>{esc(u["footer_tagline"])}</p>
      </div>
      <div>
        <h4>{esc(u["footer_services"])}</h4>
        <ul>{serv_links}</ul>
      </div>
      <div>
        <h4>{esc(u["footer_clinic"])}</h4>
        <ul>
          <li><a href="{home}sobre-nosotros/">{esc(u["footer_about"])}</a></li>
          <li><a href="{home}programas/">{esc(u["menu"]["programas"])}</a></li>
          <li><a href="{home}blog/">{esc(u["footer_blog"])}</a></li>
          <li><a href="{home}contacto/">{esc(u["footer_contact"])}</a></li>
          {legal_lis}
        </ul>
      </div>
      <div>
        <h4>{esc(u["footer_contact"])}</h4>
        <ul>
          {phones}
          <li>{CONTACT["address_html"]}</li>
        </ul>
      </div>
    </div>
    <p class="footer__legal-note">{u["legal_note"]}</p>
    <div class="footer__bottom">
      <div>{esc(u["copyright"])} · {legal}</div>
      <div class="socials">
        <a href="{CONTACT["instagram"]}" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
        <a href="{CONTACT["facebook"]}" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2 0-3 1-3 3v2H9v3h2v6h3v-6h2.5l.5-3H14v-1c0-.6.4-1 1-1z"/></svg></a>
        <a href="https://wa.me/{CONTACT["whatsapp"]}" aria-label="WhatsApp">{WA_SVG}</a>
      </div>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{CONTACT["whatsapp"]}" aria-label="WhatsApp" target="_blank" rel="noopener">{WA_SVG}</a>

<nav class="mobile-cta" aria-label="{esc(_BOOK_LABEL[lang])}">
  <a class="mobile-cta__item" href="tel:{CONTACT["phones_tel"][0]}">{_TEL_SVG}<span>{esc(_CALL_LABEL[lang])}</span></a>
  <a class="mobile-cta__item" href="https://wa.me/{CONTACT["whatsapp"]}" target="_blank" rel="noopener">{WA_SVG}<span>WhatsApp</span></a>
  <a class="mobile-cta__item mobile-cta__book" href="{home}#cita">{_CAL_SVG}<span>{esc(_BOOK_LABEL[lang])}</span></a>
</nav>

<div id="cookie-banner" class="cookie-banner" hidden role="dialog" aria-label="Cookies">
  <p>{esc(u["cookie_text"])} <a href="{home}politica-de-cookies/">{esc(u["cookie_more"])}</a></p>
  <div class="cookie-banner__btns">
    <button class="btn btn-ghost" type="button" onclick="impulsCookie(false)">{esc(u["cookie_reject"])}</button>
    <button class="btn btn-primary" type="button" onclick="impulsCookie(true)">{esc(u["cookie_accept"])}</button>
  </div>
</div>
<script>
function impulsCookie(ok){{try{{localStorage.setItem('impuls_consent',ok?'accepted':'rejected');}}catch(e){{}}var b=document.getElementById('cookie-banner');if(b)b.hidden=true;if(ok&&window.__impulsLoadAnalytics)window.__impulsLoadAnalytics();}}
function impulsSubmit(f){{
  if(f._gotcha&&f._gotcha.value)return false;
  var AMO="{AMO_ENDPOINT}",FID="{AMO_FORM_ID}",HASH="{AMO_HASH}";
  var v=function(n){{var el=f.querySelector('[name="'+n+'"]');return el?String(el.value).trim():'';}};
  if(!FID||!HASH){{f.classList.add('is-sent');return false;}}
  var nota='Solicitud desde: '+document.title+' — '+location.href;
  var msg=v('mensaje');if(msg)nota+=' · Mensaje: '+msg;
  nota+=' · Idioma: '+v('idioma');
  var p=new URLSearchParams();
  p.append('form_id',FID);p.append('hash',HASH);
  p.append('fields[name_1]',v('nombre'));
  p.append('fields[949379_1][682993]',(v('phone_code')+' '+v('telefono')).trim());
  p.append('fields[949381_1][683005]',v('email'));
  p.append('fields[note_2]',nota);
  p.append('user_origin','');p.append('robots','');
  var b=f.querySelector('button[type=submit]');if(b)b.disabled=true;
  fetch(AMO,{{method:'POST',mode:'no-cors',headers:{{'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}},body:p.toString()}})
   .then(function(){{f.classList.add('is-sent');f.reset();if(typeof window.fbq==='function')window.fbq('track','Lead');if(typeof window.gtag==='function')window.gtag('event','generate_lead');}})
   .then(null,function(){{if(b)b.disabled=false;}});
  return false;
}}
(function(){{try{{if(!localStorage.getItem('impuls_consent')){{var b=document.getElementById('cookie-banner');if(b)b.hidden=false;}}}}catch(e){{}}}})();
</script>
</body>
</html>'''

def icon(slug):
    from content import ICONS
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7">{ICONS[slug]}</svg>'

def redirect_page(url):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta http-equiv="refresh" content="0; url={url}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="noindex, follow" />
<title>Impuls Longevity</title>
<script>location.replace("{url}");</script>
</head>
<body>Redirigiendo a <a href="{url}">{url}</a>…</body>
</html>'''

# ---------- Página principal ----------
def render_home(lang):
    c = HOME_CONTENT[lang]; u = UI[lang]; home = HOME[lang]
    alts = {L: HOME[L] for L in LANGS}
    out = head(lang, c["title"], c["description"], home, alts, faq=c["faq"])
    out += header(lang, alts)
    # hero
    trust = "".join(f'<div><div class="num">{esc(n)}</div><div class="lbl">{esc(l)}</div></div>' for n, l in c["trust"])
    out += f'''<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <span class="eyebrow">{esc(c["hero_eyebrow"])}</span>
      <h1>{esc(c["hero_h1_a"])} <span class="accent">{esc(c["hero_h1_accent"])}</span></h1>
      <p class="hero__lead">{esc(c["hero_lead"])}</p>
      <div class="hero__actions">
        <a class="btn btn-primary" href="#cita">{esc(c["hero_cta1"])}</a>
        <a class="btn btn-ghost" href="#servicios">{esc(c["hero_cta2"])}</a>
      </div>
      <div class="hero__trust">{trust}</div>
    </div>
    <div class="hero__media"><img src="/assets/hero-procedure.jpg" alt="Tratamiento láser facial en Impuls Longevity Barcelona" /></div>
  </div>
</section>
<div class="brands"><div class="container brands__row">{"".join(f"<span>{esc(b)}</span>" for b in BRANDS)}</div></div>
'''
    # servicios (+ отдельный блок «Salud y bienestar» для wellness-услуг)
    def _card(s):
        d = s[lang]
        if s.get("external"):
            href, attrs, arrow = s["external"], ' target="_blank" rel="noopener"', "↗"
        else:
            href, attrs, arrow = f'{home}{s["slug"]}/', '', "→"
        # Wellness (Salud y bienestar): tarjeta con icono, como antes de las fotos.
        if s.get("group") == "wellness":
            return f'''<article class="card">
        <div class="card__icon">{icon(s["slug"])}</div>
        <h3>{esc(d["name"])}</h3>
        <p>{esc(d["tag"])}</p>
        <a class="card__link" href="{href}"{attrs}>{esc(d["name"])} {arrow}</a>
      </article>'''
        # Servicios láser: foto real arriba (assets/cards/<slug>.jpg, optimizadas ~760px).
        # alt descriptivo (SEO) y lazy + aspect-ratio en CSS para no romper CLS.
        photo = f'/assets/cards/{s["slug"]}.jpg'
        alt = esc(f'{d["name"]} · Impuls Longevity Barcelona')
        # Destacado premium (marco dorado + pestaña) para tratamientos estrella: 4Glow, 4D Fotona.
        badge = s.get("badge")
        feat, tab = "", ""
        if badge and badge.get(lang):
            feat = " card--featured"
            star = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.8 5.9 20.4l1.5-6.8L2.2 9l6.9-.7z"/></svg>'
            tab = f'<span class="card__tab">{star}{esc(badge[lang])}</span>'
        return f'''<article class="card card--photo{feat}">
        {tab}<div class="card__media"><img src="{photo}" alt="{alt}" loading="lazy" decoding="async" /></div>
        <div class="card__body">
        <h3>{esc(d["name"])}</h3>
        <p>{esc(d["tag"])}</p>
        <a class="card__link" href="{href}"{attrs}>{esc(d["name"])} {arrow}</a>
        </div>
      </article>'''
    cards = "".join(_card(s) for s in SERVICES if s.get("group") != "wellness")
    wellness = "".join(_card(s) for s in SERVICES if s.get("group") == "wellness")
    out += f'''<section class="section" id="servicios">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{esc(c["services_eyebrow"])}</span>
      <h2>{esc(c["services_h2"])}</h2>
      <p>{esc(c["services_p"])}</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>
'''
    if wellness:
        out += f'''<section class="section section--wellness" id="bienestar">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{esc(c["wellness_eyebrow"])}</span>
      <h2>{esc(c["wellness_h2"])}</h2>
      <p>{esc(c["wellness_p"])}</p>
    </div>
    <div class="cards">{wellness}</div>
  </div>
</section>
'''
    # seguridad
    checklist = "".join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg><span>{esc(x)}</span></li>' for x in c["safety_list"])
    out += f'''<section class="section section--mint">
  <div class="container split">
    <div class="split__media"><img src="/assets/treatment.jpg" alt="Impuls Longevity" loading="lazy" /></div>
    <div class="split__text">
      <span class="eyebrow">{esc(c["safety_eyebrow"])}</span>
      <h2>{esc(c["safety_h2"])}</h2>
      <p>{esc(c["safety_p"])}</p>
      <ul class="checklist">{checklist}</ul>
    </div>
  </div>
</section>
'''
    # tecnología
    techs = "".join(f'<div class="tech"><div class="k">{esc(k)}</div><p>{esc(v)}</p></div>' for k, v in c["tech_items"])
    out += f'''<section class="section" id="tecnologia">
  <div class="container split">
    <div class="split__text">
      <span class="eyebrow">{esc(c["tech_eyebrow"])}</span>
      <h2>{esc(c["tech_h2"])}</h2>
      <p>{esc(c["tech_p"])}</p>
    </div>
    <div class="split__media"><img src="/assets/tech-fotona.jpg" alt="Láser Fotona StarWalker y SP Dynamis en Impuls Longevity Barcelona" loading="lazy" decoding="async" /></div>
  </div>
  <div class="container tech-grid-wrap">
    <div class="tech-grid">{techs}</div>
  </div>
</section>
'''
    # por qué (confianza)
    whys = "".join(f'<div class="why"><div class="why__n">{esc(n)}</div><h3>{esc(t)}</h3><p>{esc(dd)}</p></div>' for n, t, dd in c["why_items"])
    out += f'''<section class="section section--mint">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(c["why_eyebrow"])}</span><h2>{esc(c["why_h2"])}</h2></div>
    <div class="why-grid">{whys}</div>
  </div>
</section>
'''
    # faq
    faqs = "".join(f'<details{" open" if i==0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(c["faq"]))
    out += f'''<section class="section" id="faq">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{esc(c["faq_eyebrow"])}</span>
      <h2>{esc(c["faq_h2"])}</h2>
    </div>
    <div class="faq">{faqs}</div>
  </div>
</section>
'''
    # opiniones (prueba social real de Google) — justo antes del formulario
    rv = REVIEW_UI[lang]
    STAR = '<svg class="rv-star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.7-5.2 4.6 1.5 6.8L12 17.8 5.9 20.4l1.5-6.8L2.2 9l6.9-.7z"/></svg>'
    rev_cards = ""
    for r in REVIEWS:
        stars = f'<div class="review__stars" role="img" aria-label="{r["stars"]}/5">' + STAR * r["stars"] + '</div>'
        rev_cards += f'''<article class="review">
        <div class="review__head">
          <span class="review__ava" aria-hidden="true">{esc(r["name"][0])}</span>
          <div class="review__id"><span class="review__name">{esc(r["name"])}</span>{stars}</div>
          <span class="review__src">{esc(rv["src"])}</span>
        </div>
        <p class="review__text">{esc(r["text"])}</p>
      </article>'''
    out += f'''<section class="section" id="opiniones">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(rv["eyebrow"])}</span><h2>{esc(rv["h2"])}</h2></div>
    <div class="reviews">{rev_cards}</div>
    <p class="reviews__note">{esc(rv["note"])}</p>
  </div>
</section>
'''
    out += cta_form(lang, "home")
    out += footer(lang)
    return out

# ---------- Enlazado interno: servicios relacionados ----------
# Mejora el SEO on-page distribuyendo autoridad entre páginas temáticamente próximas.
# Solo apunta a servicios internos (sin "external"), para no enviar el link fuera del sitio.
RELATED = {
    "eliminacion-de-tatuajes": ["eliminacion-de-pigmentacion", "rejuvenecimiento-cutaneo", "cicatrices-y-estrias"],
    "rejuvenecimiento-cutaneo": ["cicatrices-y-estrias", "eliminacion-de-pigmentacion", "tratamiento-del-acne"],
    "eliminacion-de-pigmentacion": ["eliminacion-de-tatuajes", "rejuvenecimiento-cutaneo", "tratamiento-del-acne"],
    "depilacion-laser": ["rejuvenecimiento-cutaneo", "aranas-vasculares-rosacea", "tratamiento-del-acne"],
    "tratamiento-del-acne": ["cicatrices-y-estrias", "eliminacion-de-pigmentacion", "rejuvenecimiento-cutaneo"],
    "aranas-vasculares-rosacea": ["rejuvenecimiento-cutaneo", "tratamiento-del-acne", "depilacion-laser"],
    "cicatrices-y-estrias": ["rejuvenecimiento-cutaneo", "tratamiento-del-acne", "eliminacion-de-pigmentacion"],
    "onicomicosis": ["eliminacion-de-neoplasias", "depilacion-laser", "aranas-vasculares-rosacea"],
    "eliminacion-de-neoplasias": ["onicomicosis", "cicatrices-y-estrias", "eliminacion-de-pigmentacion"],
}
_RELATED_LABEL = {"es": "Servicios relacionados", "ca": "Serveis relacionats", "ru": "Похожие услуги", "en": "Related services"}
_MORE_LABEL = {"es": "Más sobre este tratamiento", "ca": "Més sobre aquest tractament", "ru": "Подробнее об этой процедуре", "en": "More about this treatment"}
_CALL_LABEL = {"es": "Llamar", "ca": "Trucar", "ru": "Позвонить", "en": "Call"}
_BOOK_LABEL = {"es": "Pedir cita", "ca": "Demana cita", "ru": "Записаться", "en": "Book"}
_TEL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3-8.6A2 2 0 014.1 2h3a2 2 0 012 1.7c.1.9.3 1.8.6 2.7a2 2 0 01-.5 2.1L8.1 9.6a16 16 0 006 6l1.1-1.1a2 2 0 012.1-.5c.9.3 1.8.5 2.7.6a2 2 0 011.7 2z"/></svg>'
_CAL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'

def related_services(lang, s):
    slugs = RELATED.get(s["slug"], [])
    if not slugs:
        return ""
    home = HOME[lang]
    by_slug = {x["slug"]: x for x in SERVICES}
    cards = ""
    for sl in slugs:
        rs = by_slug.get(sl)
        if not rs or rs.get("external"):
            continue
        d = rs[lang]
        cards += f'''<article class="card">
        <div class="card__icon">{icon(sl)}</div>
        <h3>{esc(d["name"])}</h3>
        <p>{esc(d["tag"])}</p>
        <a class="card__link" href="{home}{sl}/">{esc(d["name"])} →</a>
      </article>'''
    if not cards:
        return ""
    return f'''<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(_RELATED_LABEL[lang])}</span><h2>{esc(_RELATED_LABEL[lang])}</h2></div>
    <div class="cards">{cards}</div>
  </div>
</section>
'''

# ---------- Página de servicio ----------
def render_service(lang, s):
    d = s[lang]; u = UI[lang]; home = HOME[lang]; slug = s["slug"]
    alts = {L: f'{HOME[L]}{slug}/' for L in LANGS}
    _low = d["name"].lower()
    if "láser" in _low or "làser" in _low or "laser" in _low or "лазер" in _low or "fotona" in _low:
        title = f'{d["name"]}{u["seo_h1_geo"]} · Impuls'
    else:
        title = f'{d["name"]} {u["seo_title_suffix"]} · Impuls'
    desc = f'{d["tag"]}. {u["seo_desc_suffix"]}'
    out = head(lang, title, desc, alts[lang], alts, faq=d.get("faq"))
    out += header(lang, alts)
    # hero servicio
    intro = "".join(f"<p>{esc(p)}</p>" for p in d["intro"])
    benefits = "".join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg><span>{esc(b)}</span></li>' for b in d["benefits"])
    out += f'''<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <span class="eyebrow"><a href="{home}#servicios" style="color:inherit">{esc(u["menu"]["servicios"])}</a></span>
      <h1>{esc(d["name"] + u["seo_h1_geo"])}</h1>
      <p class="hero__lead">{esc(d["tag"])}</p>
      <div class="hero__actions">
        <a class="btn btn-primary" href="#cita">{esc(u["cta_nav"])}</a>
        <a class="btn btn-ghost" href="{home}#servicios">{esc(u["all_services"])}</a>
      </div>
    </div>
    <div class="hero__media"><img src="{s["img"]}" alt="{esc(d["name"])} · Impuls Longevity" /></div>
  </div>
</section>
'''
    # intro + beneficios
    out += f'''<section class="section section--mint">
  <div class="container split">
    <div class="split__text">
      <span class="eyebrow">{esc(u["benefits_title"])}</span>
      {intro}
      <ul class="checklist">{benefits}</ul>
    </div>
    <div class="split__media"><img src="{s.get("img2", s["img"])}" alt="{esc(d["name"])} · Impuls Longevity" loading="lazy" /></div>
  </div>
</section>
'''
    # cómo funciona
    steps = ""
    for i, (t, ds) in enumerate(d["steps"], 1):
        steps += f'''<article class="card">
        <div class="card__icon">{i}</div>
        <h3>{esc(t)}</h3>
        <p>{esc(ds)}</p>
      </article>'''
    out += f'''<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(u["how_title"])}</span><h2>{esc(u["how_title"])}</h2></div>
    <div class="cards">{steps}</div>
  </div>
</section>
'''
    # tecnología usada (chips)
    chips = "".join(f'<div class="tech"><div class="k">{esc(t)}</div></div>' for t in d["tech"])
    out += f'''<section class="section section--mint">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(u["tech_used_title"])}</span><h2>{esc(u["tech_used_title"])}</h2></div>
    <div class="tech-grid">{chips}</div>
  </div>
</section>
'''
    # faq
    faqs = "".join(f'<details{" open" if i==0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(d["faq"]))
    out += f'''<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(u["faq_title"])}</span><h2>{esc(u["faq_title"])}</h2></div>
    <div class="faq">{faqs}</div>
  </div>
</section>
'''
    out += related_services(lang, s)
    out += cta_form(lang, slug)
    out += footer(lang)
    return out

# ---------- Página "Sobre nosotros" ----------
def render_about(lang):
    a = ABOUT[lang]; u = UI[lang]; home = HOME[lang]
    alts = {L: f"{HOME[L]}sobre-nosotros/" for L in LANGS}
    out = head(lang, a["title"], a["description"], alts[lang], alts)
    out += header(lang, alts)
    trust = "".join(f'<div><div class="num">{esc(n)}</div><div class="lbl">{esc(l)}</div></div>' for n, l in a["stats"])
    out += f'''<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <span class="eyebrow">{esc(a["eyebrow"])}</span>
      <h1>{esc(a["h1"])}</h1>
      <p class="hero__lead">{esc(a["lead"])}</p>
      <div class="hero__trust">{trust}</div>
    </div>
    <div class="hero__media"><img src="/assets/about-hero.jpg" alt="Consulta personalizada en Impuls Longevity Barcelona" /></div>
  </div>
</section>
<section class="section section--mint">
  <div class="container">
    <div class="section-head"><span class="eyebrow">{esc(a["team_eyebrow"])}</span><h2>{esc(a["team_h2"])}</h2><p>{esc(a["team_p"])}</p></div>
    <div class="team-photo"><img src="/assets/team.jpg" alt="{esc(a["team_h2"])}" loading="lazy" /></div>
  </div>
</section>
'''
    sections = ""
    for h, paras in a["sections"]:
        sections += f'<div class="prose"><h2>{esc(h)}</h2>' + "".join(f"<p>{esc(p)}</p>" for p in paras) + "</div>"
    out += f'<section class="section"><div class="container">{sections}</div></section>\n'
    values = "".join(f'<article class="card"><h3>{esc(t)}</h3><p>{esc(dd)}</p></article>' for t, dd in a["values"])
    out += f'''<section class="section section--mint">
  <div class="container">
    <div class="cards">{values}</div>
  </div>
</section>
'''
    out += cta_form(lang, "sobre-nosotros")
    out += footer(lang)
    return out

# ---------- Página "Contacto" ----------
def render_contact(lang):
    p = CONTACTP[lang]; u = UI[lang]; home = HOME[lang]
    alts = {L: f"{HOME[L]}contacto/" for L in LANGS}
    out = head(lang, p["title"], p["description"], alts[lang], alts)
    out += header(lang, alts)
    phones = "".join(f'<p><a href="tel:{t}">{esc(ph)}</a></p>' for ph, t in zip(CONTACT["phones"], CONTACT["phones_tel"]))
    hours = "".join(f"<li>{esc(h)}</li>" for h in p["hours"])
    hours_note_html = f'<p><small>{esc(p["hours_note"])}</small></p>' if p.get("hours_note") else ""
    mapq = "Pl.+d'Urquinaona,+6,+08010+Barcelona"
    out += f'''<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <span class="eyebrow">{esc(p["eyebrow"])}</span>
      <h1>{esc(p["h1"])}</h1>
      <p class="hero__lead">{esc(p["lead"])}</p>
    </div>
    <div class="hero__media"><img src="/assets/barcelona.jpg" alt="Barcelona · Impuls Longevity" /></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="cards">
      <article class="card">
        <h3>{esc(p["address_title"])}</h3>
        <p>{CONTACT["address_html"]}</p>
      </article>
      <article class="card">
        <h3>{esc(p["phone_title"])}</h3>
        {phones}
        <p><a href="https://wa.me/{CONTACT["whatsapp"]}">WhatsApp</a></p>
      </article>
      <article class="card">
        <h3>{esc(p["hours_title"])}</h3>
        <ul class="hours">{hours}</ul>
        {hours_note_html}
      </article>
    </div>
    <div class="map"><iframe src="https://www.google.com/maps?q={mapq}&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa Impuls Longevity"></iframe></div>
  </div>
</section>
'''
    out += cta_form(lang, "contacto")
    out += footer(lang)
    return out

# ---------- Páginas legales ----------
def _emph(t):
    """Resalta importes en € y plazos clave (24 h / 30 días) para facilitar la lectura."""
    t = re.sub(r'(\d+\s?€)', r'<strong>\1</strong>', t)
    t = re.sub(r'\b(24\s?(?:horas|hores|hours|часа))\b', r'<strong>\1</strong>', t)
    t = re.sub(r'\b(30\s?(?:días|dies|days|дней))\b', r'<strong>\1</strong>', t)
    return t

_TOC_LABEL = {"es": "Contenido", "ca": "Contingut", "ru": "Содержание", "en": "Contents"}
_TOP_LABEL = {"es": "Volver arriba", "ca": "Tornar amunt", "ru": "Наверх", "en": "Back to top"}

def render_legal(lang, slug):
    p = LEGAL[slug][lang]
    alts = {L: f"{HOME[L]}{slug}/" for L in LANGS}
    _first = p["blocks"][0][1][0] if p.get("blocks") and p["blocks"][0][1] else ""
    desc = (f'{p["h1"]} · Impuls Longevity. {_first}')[:158]
    out = head(lang, p["title"], desc, alts[lang], alts)
    out += header(lang, alts)
    note = TRANS_NOTE[lang]
    note_html = f'<p class="prose" style="color:var(--muted);font-size:.9rem">{esc(note)}</p>' if note else ""
    toc_items = ""
    blocks = ""
    for i, (h, paras) in enumerate(p["blocks"], 1):
        anchor = f"s{i}"
        toc_items += f'<li><a href="#{anchor}">{esc(h)}</a></li>'
        blocks += f'<div class="prose"><h2 id="{anchor}">{esc(h)}</h2>' + "".join(f"<p>{_emph(esc(x))}</p>" for x in paras) + "</div>"
    toc = f'<nav class="toc" aria-label="{esc(_TOC_LABEL[lang])}"><h2>{esc(_TOC_LABEL[lang])}</h2><ul>{toc_items}</ul></nav>'
    out += f'''<section class="hero"><div class="container">
    <h1 id="top">{esc(p["h1"])}</h1>
    <p class="hero__lead">{esc(UPDATED[lang])}</p>
  </div></section>
<section class="section"><div class="container">{note_html}{toc}{blocks}</div></section>
<a href="#top" class="to-top" aria-label="{esc(_TOP_LABEL[lang])}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg></a>
<script>(function(){{var b=document.querySelector('.to-top');if(!b)return;window.addEventListener('scroll',function(){{b.classList.toggle('is-visible',window.scrollY>500);}});}})();</script>
'''
    out += footer(lang)
    return out

# ---------- Página de programas ----------
def render_promo(lang):
    p = PROMO[lang]; u = UI[lang]
    alts = {L: f"{HOME[L]}programas/" for L in LANGS}
    out = head(lang, p["title"], p["description"], alts[lang], alts)
    out += header(lang, alts)
    out += f'''<section class="hero"><div class="container">
    <span class="eyebrow">{esc(p["eyebrow"])}</span>
    <h1>{esc(p["h1"])}</h1>
    <p class="hero__lead">{esc(p["lead"])}</p>
  </div></section>
'''
    imgs = ["/assets/program-pigment.jpg", "/assets/program-lift.jpg", "/assets/program-pigmentcontrol.jpg"]
    blocks = ""
    for idx, pr in enumerate(p["featured"]):
        rev = " program--rev" if idx % 2 else ""
        img = imgs[idx] if idx < len(imgs) else imgs[-1]
        desc = "".join(f"<p>{esc(x)}</p>" for x in pr["desc"])
        items = "".join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg><span>{esc(x)}</span></li>' for x in pr["list"])
        rows = ""
        for lbl, amt, note in pr["price"]:
            note_html = f'<small>{esc(note)}</small>' if note else ""
            rows += f'<div class="program__price-line"><span>{esc(lbl)}</span><b>{esc(amt)}{note_html}</b></div>'
        blocks += f'''<article class="program{rev}">
      <div class="program__media"><img src="{img}" alt="{esc(pr["name"])} · Impuls Longevity" loading="lazy" /></div>
      <div class="program__content">
        <span class="program__badge">{esc(pr["badge"])}</span>
        <h2>{esc(pr["name"])}</h2>
        <p class="program__tag">{esc(pr["tag"])}</p>
        <div class="program__desc">{desc}</div>
        <h4 class="program__list-title">{esc(pr["list_title"])}</h4>
        <ul class="program__list">{items}</ul>
        <div class="program__pricing">{rows}</div>
        <a class="btn btn-primary" href="#cita">{esc(u["cta_nav"])}</a>
      </div>
    </article>'''
    dg = p["diag"]
    dg_prices = "".join(f'<div class="diag__price"><span>{esc(l)}</span><b>{esc(pr)}</b></div>' for l, pr in dg["prices"])
    diag_html = f'''<div class="diag">
      <div class="diag__prices">{dg_prices}</div>
      <div class="diag__text"><p>{esc(dg["note"])}</p><p class="diag__cond">{esc(dg["cond"])}</p></div>
    </div>'''
    cb = p["club"]
    club_html = f'''<div class="club">
      <span class="club__badge">{esc(cb["badge"])}</span>
      <h3 class="club__title">{esc(cb["title"])}</h3>
      <p class="club__text">{esc(cb["text"])}</p>
    </div>'''
    out += f'''<section class="section"><div class="container">
    {blocks}
    {club_html}
    {diag_html}
    <p class="prose" style="margin-top:20px">{esc(p["cta_note"])}</p>
  </div></section>
'''
    out += cta_form(lang, "programas")
    out += footer(lang)
    return out

# ---------- Blog ----------
def render_blog_index(lang):
    b = BLOG_INDEX[lang]; home = HOME[lang]
    alts = {L: f"{HOME[L]}blog/" for L in LANGS}
    out = head(lang, b["title"], b["description"], alts[lang], alts)
    out += header(lang, alts)
    out += f'''<section class="hero"><div class="container">
    <span class="eyebrow">{esc(b["eyebrow"])}</span>
    <h1>{esc(b["h1"])}</h1>
    <p class="hero__lead">{esc(b["lead"])}</p>
  </div></section>
'''
    cards = ""
    for post in BLOG_POSTS:
        d = post[lang]
        cards += f'''<article class="card">
        <h3>{esc(d["title"])}</h3>
        <p>{esc(d["excerpt"])}</p>
        <a class="card__link" href="{home}blog/{post["slug"]}/">{esc(b["read"])} →</a>
      </article>'''
    out += f'<section class="section"><div class="container"><div class="cards">{cards}</div></div></section>\n'
    out += footer(lang)
    return out

def render_post(lang, post):
    d = post[lang]; b = BLOG_INDEX[lang]; home = HOME[lang]; slug = post["slug"]
    alts = {L: f"{HOME[L]}blog/{slug}/" for L in LANGS}
    out = head(lang, f'{d["title"]} · Impuls', d["excerpt"], alts[lang], alts)
    out += header(lang, alts)
    out += f'''<section class="hero"><div class="container hero__grid">
    <div class="hero__content">
      <span class="eyebrow"><a href="{home}blog/" style="color:inherit">{esc(b["eyebrow"])}</a></span>
      <h1>{esc(d["title"])}</h1>
      <p class="hero__lead">{esc(d["excerpt"])}</p>
    </div>
    <div class="hero__media"><img src="{post["img"]}" alt="{esc(d["title"])}" /></div>
  </div></section>
'''
    body = ""
    for h, paras in d["sections"]:
        block = '<div class="prose">'
        if h:
            block += f"<h2>{esc(h)}</h2>"
        block += "".join(f"<p>{esc(x)}</p>" for x in paras) + "</div>"
        body += block
    if post.get("sources"):
        links = "".join(f'<li><a href="{url}" target="_blank" rel="noopener nofollow">{esc(name)}</a></li>' for name, url in post["sources"])
        body += f'<div class="prose sources"><h2>{esc(b["sources"])}</h2><ul>{links}</ul><p><small>{esc(b["sources_note"])}</small></p></div>'
    sv = post.get("service")
    if sv:
        svc = next((x for x in SERVICES if x["slug"] == sv and not x.get("external")), None)
        if svc:
            body += f'<div class="prose"><p><a href="{home}{sv}/">{esc(_MORE_LABEL[lang])}: {esc(svc[lang]["name"])} →</a></p></div>'
    out += f'<section class="section"><div class="container">{body}</div></section>\n'
    out += cta_form(lang, f"blog-{slug}")
    out += footer(lang)
    return out

# ---------- Escritura ----------
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def rel(lang, sub=""):
    """Ruta de carpeta relativa por idioma: es -> raíz, ru -> ru/, en -> en/."""
    base = "" if lang == "es" else f"{lang}/"
    return f"{base}{sub}"

def main():
    written = []
    urls = []  # solo páginas indexables (sin los redirects noindex)

    def add(path, content, index=True):
        written.append(write(path, content))
        if index:
            tail = path[:-len("index.html")] if path.endswith("index.html") else path
            urls.append(f"{DOMAIN}/{tail}")

    for lang in LANGS:
        add(rel(lang, "index.html"), render_home(lang))
        add(rel(lang, "sobre-nosotros/index.html"), render_about(lang))
        add(rel(lang, "contacto/index.html"), render_contact(lang))
        add(rel(lang, "programas/index.html"), render_promo(lang))
        add(rel(lang, "blog/index.html"), render_blog_index(lang))
        for post in BLOG_POSTS:
            add(rel(lang, f'blog/{post["slug"]}/index.html'), render_post(lang, post))
        for slug in LEGAL:
            add(rel(lang, f"{slug}/index.html"), render_legal(lang, slug))
        for s in SERVICES:
            if s.get("external"):
                # servicio con sitio propio: redirect noindex, fuera del sitemap
                add(rel(lang, f'{s["slug"]}/index.html'), redirect_page(s["external"]), index=False)
                continue
            add(rel(lang, f'{s["slug"]}/index.html'), render_service(lang, s))

    # sitemap.xml + robots.txt (SEO: continuidad al migrar desde Tilda)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc></url>")
    sm.append("</urlset>")
    written.append(write("sitemap.xml", "\n".join(sm) + "\n"))
    written.append(write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n"))

    print(f"Generadas {len(written)} páginas (indexables en sitemap: {len(urls)}).")

if __name__ == "__main__":
    main()
