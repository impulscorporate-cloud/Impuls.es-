# -*- coding: utf-8 -*-
"""
Impuls Longevity — blog (índice + 3 artículos) en ES / RU / EN.
Contenido basado en los artículos del sitio original.
"""

BLOG_INDEX = {
    "es": {"title": "Blog · Impuls Longevity", "description": "Cuidado de tu piel: consejos sobre rosácea, protección solar y antiedad por Impuls Longevity.", "eyebrow": "Blog", "h1": "Cuidado de tu piel", "lead": "Consejos y guías de nuestros especialistas para cuidar tu piel con criterio.", "read": "Leer artículo", "sources": "Fuentes", "sources_note": "Enlaces a organizaciones de referencia para ampliar información. Contenido divulgativo, no sustituye una valoración médica."},
    "ca": {"title": "Blog · Impuls Longevity", "description": "Cura de la teva pell: consells sobre rosàcia, protecció solar i antienvelliment per Impuls Longevity.", "eyebrow": "Blog", "h1": "Cura de la teva pell", "lead": "Consells i guies dels nostres especialistes per cuidar la teva pell amb criteri.", "read": "Llegeix l'article", "sources": "Fonts", "sources_note": "Enllaços a organitzacions de referència per ampliar informació. Contingut divulgatiu, no substitueix una valoració mèdica."},
    "ru": {"title": "Блог · Impuls Longevity", "description": "Уход за кожей: розацеа, защита от солнца и антиэйдж от специалистов Impuls Longevity.", "eyebrow": "Блог", "h1": "Уход за кожей", "lead": "Советы и гайды наших специалистов, как ухаживать за кожей осознанно.", "read": "Читать статью", "sources": "Источники", "sources_note": "Ссылки на авторитетные организации для дополнительного чтения. Материал ознакомительный, не заменяет очную консультацию."},
    "en": {"title": "Blog · Impuls Longevity", "description": "Skincare tips on rosacea, sun protection and anti-ageing by Impuls Longevity.", "eyebrow": "Blog", "h1": "Caring for your skin", "lead": "Advice and guides from our specialists to care for your skin wisely.", "read": "Read article", "sources": "Sources", "sources_note": "Links to reference organisations for further reading. Educational content, not a substitute for a medical assessment."},
}

BLOG_POSTS = [
    {
        "slug": "rosacea-9-errores",
        "img": "/assets/hero.jpg",
        "es": {
            "title": "Rosácea: 9 errores que arruinan tu piel",
            "excerpt": "La rosácea es una enfermedad crónica de la piel. Descubre qué debes evitar y cómo aliviarla.",
            "sections": [
                ("", ["La rosácea es una enfermedad cutánea crónica: provoca inflamación vascular que se manifiesta como enrojecimiento o síntomas similares al acné. La genética es la causa principal y, como toda enfermedad crónica, alterna remisiones y brotes. El objetivo del tratamiento es inducir la remisión, no una cura definitiva."]),
                ("Los 9 errores más frecuentes", [
                    "1. Limpiadores agresivos. Aguas micelares y aceites hidrofílicos dañan una barrera ya comprometida; mejor geles suaves.",
                    "2. Descuidar el cuidado en casa. La piel necesita restauración activa, no solo limpieza.",
                    "3. Procedimientos prematuros. No hacer tratamientos como BBL durante un brote: primero calmar la inflamación.",
                    "4. Temperaturas extremas. Evitar saunas, vapor y duchas muy calientes que dilatan los vasos.",
                    "5. Protección solar insuficiente. La radiación UV agrava los vasos; minimiza la exposición y protégete.",
                    "6. Exfoliantes físicos. Cepillos y dispositivos crean microdesgarros y sobreestimulan los capilares.",
                    "7. Dieta sin criterio. Según tolerancia, limitar tomate, vino tinto y comidas muy picantes o calientes.",
                    "8. Estrés crónico. Es uno de los desencadenantes más fuertes; ayudan la gestión del estrés y el descanso.",
                    "9. Automedicación. Activos potentes (p. ej. Rozex, Soolantra) requieren supervisión profesional.",
                ]),
                ("", ["¿Tienes rosácea o piel reactiva? En Impuls Longevity valoramos tu caso y diseñamos un protocolo seguro y personalizado."]),
            ],
        },
        "ca": {
            "title": "Rosàcia: 9 errors que arruïnen la teva pell",
            "excerpt": "La rosàcia és una malaltia crònica de la pell. Descobreix què has d'evitar i com alleujar-la.",
            "sections": [
                ("", ["La rosàcia és una malaltia cutània crònica: provoca inflamació vascular que es manifesta com envermelliment o símptomes similars a l'acne. La genètica és la causa principal i, com tota malaltia crònica, alterna remissions i brots. L'objectiu del tractament és induir la remissió, no una cura definitiva."]),
                ("Els 9 errors més freqüents", [
                    "1. Netejadors agressius. Aigües micel·lars i olis hidrofílics danyen una barrera ja compromesa; millor gels suaus.",
                    "2. Descuidar la cura a casa. La pell necessita restauració activa, no només neteja.",
                    "3. Procediments prematurs. No fer tractaments com BBL durant un brot: primer calmar la inflamació.",
                    "4. Temperatures extremes. Evitar saunes, vapor i dutxes molt calentes que dilaten els vasos.",
                    "5. Protecció solar insuficient. La radiació UV agreuja els vasos; minimitza l'exposició i protegeix-te.",
                    "6. Exfoliants físics. Raspalls i dispositius creen microesquinços i sobreestimulen els capil·lars.",
                    "7. Dieta sense criteri. Segons tolerància, limitar tomàquet, vi negre i menjars molt picants o calents.",
                    "8. Estrès crònic. És un dels desencadenants més forts; ajuden la gestió de l'estrès i el descans.",
                    "9. Automedicació. Actius potents (p. ex. Rozex, Soolantra) requereixen supervisió professional.",
                ]),
                ("", ["Tens rosàcia o pell reactiva? A Impuls Longevity valorem el teu cas i dissenyem un protocol segur i personalitzat."]),
            ],
        },
        "ru": {
            "title": "Розацеа: 9 ошибок, которые портят кожу",
            "excerpt": "Розацеа — хроническое заболевание кожи. Разбираем, чего избегать и как облегчить состояние.",
            "sections": [
                ("", ["Розацеа — хроническое заболевание кожи: сосудистое воспаление, которое проявляется покраснением или симптомами, похожими на акне. Главная причина — генетика; как любое хроническое состояние, оно чередует ремиссии и обострения. Цель лечения — вызвать ремиссию, а не полное излечение."]),
                ("9 самых частых ошибок", [
                    "1. Агрессивное очищение. Мицеллярная вода и гидрофильные масла повреждают и без того ослабленный барьер; лучше мягкие гели.",
                    "2. Пренебрежение домашним уходом. Коже нужна активная реставрация, а не только очищение.",
                    "3. Преждевременные процедуры. Не делать BBL и подобное во время обострения — сначала снять воспаление.",
                    "4. Экстремальные температуры. Избегать саун, пара и очень горячего душа, расширяющих сосуды.",
                    "5. Недостаточная защита от солнца. УФ усугубляет сосуды; минимизируйте пребывание на солнце и защищайтесь.",
                    "6. Физические скрабы. Щётки и приборы дают микроразрывы и перевозбуждают капилляры.",
                    "7. Диета без разбора. По переносимости ограничить томаты, красное вино и очень острую/горячую еду.",
                    "8. Хронический стресс. Один из сильнейших триггеров; помогают управление стрессом и отдых.",
                    "9. Самолечение. Сильные активные вещества (напр. Rozex, Soolantra) требуют контроля специалиста.",
                ]),
                ("", ["Розацеа или реактивная кожа? В Impuls Longevity мы оценим ваш случай и составим безопасный индивидуальный протокол."]),
            ],
        },
        "en": {
            "title": "Rosacea: 9 mistakes that ruin your skin",
            "excerpt": "Rosacea is a chronic skin condition. Learn what to avoid and how to ease it.",
            "sections": [
                ("", ["Rosacea is a chronic skin disease: vascular inflammation that shows up as redness or acne-like symptoms. Genetics is the main cause and, like any chronic condition, it alternates between remission and flare-ups. The goal of treatment is to induce remission, not a definitive cure."]),
                ("The 9 most common mistakes", [
                    "1. Harsh cleansers. Micellar waters and hydrophilic oils damage an already compromised barrier; use gentle gels instead.",
                    "2. Neglecting home care. Skin needs active restoration, not just cleansing.",
                    "3. Premature procedures. Don't do treatments like BBL during a flare — calm the inflammation first.",
                    "4. Extreme temperatures. Avoid saunas, steam and very hot showers that dilate vessels.",
                    "5. Insufficient sun protection. UV worsens the vessels; minimise exposure and protect your skin.",
                    "6. Physical scrubs. Brushes and devices cause micro-tears and over-stimulate capillaries.",
                    "7. Careless diet. As tolerated, limit tomato, red wine and very spicy or hot foods.",
                    "8. Chronic stress. One of the strongest triggers; stress management and rest help.",
                    "9. Self-medication. Potent actives (e.g. Rozex, Soolantra) require professional supervision.",
                ]),
                ("", ["Do you have rosacea or reactive skin? At Impuls Longevity we assess your case and design a safe, personalised protocol."]),
            ],
        },
    },
    {
        "slug": "reglas-del-spf",
        "img": "/assets/benefits.jpg",
        "es": {
            "title": "Las verdaderas reglas del SPF que nadie te cuenta",
            "excerpt": "Protección solar para pieles sensibles y con tendencia acneica, sin provocar brotes.",
            "sections": [
                ("", ["Las recomendaciones estándar (dos líneas de producto, reaplicar cada dos horas) pueden provocar brotes en pieles acneicas por texturas pesadas y acumulación de producto. Estas son las reglas que sí funcionan."]),
                ("4 reglas clave", [
                    "1. Aplica una cantidad razonable de SPF, de forma uniforme y sin exceso.",
                    "2. Reaplica solo cuando hay exposición solar directa y prolongada.",
                    "3. Usa gel limpiador en lugar de aceites para evitar congestión.",
                    "4. Elige texturas ligeras y transpirables.",
                ]),
                ("Seguridad solar", [
                    "Aplica SPF cuando el índice UV ≥ 2. Usa sombrero cuando UV > 4 y la exposición supere 15–20 minutos. Evita la exposición directa cuando UV > 7.",
                ]),
                ("", ["¿Dudas sobre qué protección es la adecuada para tu piel? Pregúntanos en tu valoración."]),
            ],
        },
        "ca": {
            "title": "Les autèntiques regles de l'SPF que ningú t'explica",
            "excerpt": "Protecció solar per a pells sensibles i amb tendència acneica, sense provocar brots.",
            "sections": [
                ("", ["Les recomanacions estàndard (dues línies de producte, reaplicar cada dues hores) poden provocar brots en pells acneiques per textures pesades i acumulació de producte. Aquestes són les regles que sí funcionen."]),
                ("4 regles clau", [
                    "1. Aplica una quantitat raonable d'SPF, de manera uniforme i sense excés.",
                    "2. Reaplica només quan hi ha exposició solar directa i prolongada.",
                    "3. Fes servir gel netejador en lloc d'olis per evitar congestió.",
                    "4. Tria textures lleugeres i transpirables.",
                ]),
                ("Seguretat solar", [
                    "Aplica SPF quan l'índex UV ≥ 2. Fes servir barret quan UV > 4 i l'exposició superi 15–20 minuts. Evita l'exposició directa quan UV > 7.",
                ]),
                ("", ["Dubtes sobre quina protecció és adequada per a la teva pell? Pregunta'ns a la teva valoració."]),
            ],
        },
        "ru": {
            "title": "Настоящие правила SPF, о которых молчат",
            "excerpt": "Защита от солнца для чувствительной и склонной к акне кожи — без новых высыпаний.",
            "sections": [
                ("", ["Стандартные советы (два «пальца» продукта, обновлять каждые два часа) могут провоцировать высыпания на склонной к акне коже из-за тяжёлых текстур и накопления средства. Вот правила, которые действительно работают."]),
                ("4 ключевых правила", [
                    "1. Наносите разумное количество SPF — равномерно и без избытка.",
                    "2. Обновляйте только при длительном прямом солнце.",
                    "3. Смывайте гелем, а не маслом — чтобы не забивать поры.",
                    "4. Выбирайте лёгкие, дышащие текстуры.",
                ]),
                ("Безопасность на солнце", [
                    "Наносите SPF при УФ-индексе ≥ 2. Головной убор — при УФ > 4 и пребывании дольше 15–20 минут. Избегайте прямого солнца при УФ > 7.",
                ]),
                ("", ["Не уверены, какая защита подходит вашей коже? Спросите на консультации."]),
            ],
        },
        "en": {
            "title": "The real SPF rules nobody tells you",
            "excerpt": "Sun protection for sensitive, acne-prone skin — without triggering breakouts.",
            "sections": [
                ("", ["Standard advice (two lines of product, reapply every two hours) can trigger breakouts on acne-prone skin due to heavy textures and product build-up. Here are the rules that actually work."]),
                ("4 key rules", [
                    "1. Apply a reasonable amount of SPF, evenly and without excess.",
                    "2. Reapply only during prolonged direct sun exposure.",
                    "3. Use a cleansing gel instead of oils to avoid congestion.",
                    "4. Choose light, breathable textures.",
                ]),
                ("Sun safety", [
                    "Apply SPF when the UV index ≥ 2. Wear a hat when UV > 4 and exposure exceeds 15–20 minutes. Avoid direct exposure when UV > 7.",
                ]),
                ("", ["Not sure which protection suits your skin? Ask us at your assessment."]),
            ],
        },
    },
    {
        "slug": "secretos-antiedad",
        "img": "/assets/treatment.jpg",
        "es": {
            "title": "Los secretos antiedad detrás de un brillo juvenil",
            "excerpt": "8 pilares para cuidar la piel y la salud a largo plazo, con enfoque en resultados naturales.",
            "sections": [
                ("", ["Mantener una apariencia joven no depende de un único truco, sino de varios pilares que se sostienen en el tiempo. Estos son los fundamentos que trabajamos con enfoque natural y basado en evidencia."]),
                ("8 pilares antiedad", [
                    "1. Sueño de calidad: dormir entre siete y nueve horas, la herramienta antiedad más poderosa.",
                    "2. Nutrición equilibrada: proteína de calidad, carbohidratos complejos y grasas saludables.",
                    "3. Entrenamiento de fuerza: clave a partir de los 35 para mantener masa muscular.",
                    "4. Salud preventiva: corregir déficits nutricionales y reducir la inflamación.",
                    "5. Péptidos de longevidad: siempre bajo supervisión médica.",
                    "6. Sueros intravenosos: NAD+, NMN y glutatión bajo indicación profesional.",
                    "7. Salud hormonal: valorada y seguida por especialistas.",
                    "8. Cuidado estético con láser Fotona: tratamientos no invasivos para firmeza, luminosidad y contorno.",
                ]),
                ("Tratamientos Fotona que recomendamos", [
                    "En Impuls Longevity casi el 99% de nuestros procedimientos se realizan con tecnología láser Fotona, referente mundial en estética. Para el antienvejecimiento recomendamos especialmente:",
                    "Fotona 4D: efecto lifting facial sin cirugía ni inyecciones, con contracción del colágeno en profundidad.",
                    "Fotona 4Glow: mejora la luminosidad, el tono y la textura, y trata rojeces, poros y pigmentación.",
                    "SmoothEye: tensa el contorno de ojos y suaviza las arrugas periorbitales, con muy poco tiempo de recuperación.",
                    "TightSculpting: firmeza y remodelación de la piel del cuerpo.",
                    "La tecnología Fotona también ofrece NightLase (ronquido) e IntimaLase (salud íntima). Consulta con nuestro equipo el protocolo ideal para ti.",
                ]),
                ("", ["En Impuls Longevity apostamos por resultados naturales y tratamientos con evidencia. Consulta tu plan con nuestro equipo."]),
            ],
        },
        "ca": {
            "title": "Els secrets antienvelliment darrere d'una lluïssor jove",
            "excerpt": "8 pilars per cuidar la pell i la salut a llarg termini, amb enfocament en resultats naturals.",
            "sections": [
                ("", ["Mantenir una aparença jove no depèn d'un únic truc, sinó de diversos pilars que se sostenen en el temps. Aquests són els fonaments amb què treballem amb enfocament natural i basat en l'evidència."]),
                ("8 pilars antienvelliment", [
                    "1. Son de qualitat: dormir entre set i nou hores, l'eina antienvelliment més poderosa.",
                    "2. Nutrició equilibrada: proteïna de qualitat, carbohidrats complexos i greixos saludables.",
                    "3. Entrenament de força: clau a partir dels 35 per mantenir massa muscular.",
                    "4. Salut preventiva: corregir dèficits nutricionals i reduir la inflamació.",
                    "5. Pèptids de longevitat: sempre sota supervisió mèdica.",
                    "6. Sèrums intravenosos: NAD+, NMN i glutatió sota indicació professional.",
                    "7. Salut hormonal: valorada i seguida per especialistes.",
                    "8. Cura estètica amb làser Fotona: tractaments no invasius per a fermesa, lluminositat i contorn.",
                ]),
                ("Tractaments Fotona que recomanem", [
                    "A Impuls Longevity gairebé el 99% dels nostres procediments es realitzen amb tecnologia làser Fotona, referent mundial en estètica. Per a l'antienvelliment recomanem especialment:",
                    "Fotona 4D: efecte lifting facial sense cirurgia ni injeccions, amb contracció del col·lagen en profunditat.",
                    "Fotona 4Glow: millora la lluminositat, el to i la textura, i tracta rojors, porus i pigmentació.",
                    "SmoothEye: tensa el contorn d'ulls i suavitza les arrugues periorbitals, amb molt poc temps de recuperació.",
                    "TightSculpting: fermesa i remodelació de la pell del cos.",
                    "La tecnologia Fotona també ofereix NightLase (roncs) i IntimaLase (salut íntima). Consulta amb el nostre equip el protocol ideal per a tu.",
                ]),
                ("", ["A Impuls Longevity apostem per resultats naturals i tractaments amb evidència. Consulta el teu pla amb el nostre equip."]),
            ],
        },
        "ru": {
            "title": "Секреты антиэйджа за молодым сиянием",
            "excerpt": "8 опор для кожи и здоровья вдолгую — с упором на естественный результат.",
            "sections": [
                ("", ["Молодой вид — это не один трюк, а несколько опор, которые держатся во времени. Вот основы, с которыми мы работаем: естественно и на основе доказательной базы."]),
                ("8 опор антиэйджа", [
                    "1. Качественный сон: 7–9 часов — самый мощный антивозрастной инструмент.",
                    "2. Сбалансированное питание: качественный белок, сложные углеводы и полезные жиры.",
                    "3. Силовые тренировки: особенно важны после 35 для сохранения мышечной массы.",
                    "4. Профилактика: коррекция дефицитов и снижение воспаления.",
                    "5. Пептиды долголетия: только под контролем врача.",
                    "6. Внутривенные капельницы: NAD+, NMN и глутатион по показаниям специалиста.",
                    "7. Гормональное здоровье: оценка и наблюдение у специалистов.",
                    "8. Эстетический уход на лазере Fotona: неинвазивные процедуры для плотности, сияния и контура.",
                ]),
                ("Процедуры Fotona, которые мы рекомендуем", [
                    "В Impuls Longevity почти 99% процедур выполняются на лазере Fotona — мировом эталоне эстетики. Для антиэйджа особенно рекомендуем:",
                    "Fotona 4D: эффект лифтинга лица без хирургии и инъекций, с глубоким сокращением коллагена.",
                    "Fotona 4Glow: улучшает сияние, тон и текстуру, работает с покраснениями, порами и пигментацией.",
                    "SmoothEye: подтягивает контур глаз и разглаживает периорбитальные морщины, почти без периода восстановления.",
                    "TightSculpting: плотность и ремоделирование кожи тела.",
                    "Технология Fotona также предлагает NightLase (храп) и IntimaLase (интимное здоровье). Обсудите с командой идеальный протокол для вас.",
                ]),
                ("", ["В Impuls Longevity мы за естественный результат и доказательный подход. Обсудите свой план с нашей командой."]),
            ],
        },
        "en": {
            "title": "The anti-ageing secrets behind a youthful glow",
            "excerpt": "8 pillars to care for your skin and health long-term, focused on natural results.",
            "sections": [
                ("", ["A youthful look doesn't rely on a single trick, but on several pillars sustained over time. These are the fundamentals we work with — natural and evidence-based."]),
                ("8 anti-ageing pillars", [
                    "1. Quality sleep: seven to nine hours, the most powerful anti-ageing tool.",
                    "2. Balanced nutrition: quality protein, complex carbs and healthy fats.",
                    "3. Strength training: key from 35 onwards to preserve muscle mass.",
                    "4. Preventive health: correct nutritional deficits and reduce inflammation.",
                    "5. Longevity peptides: always under medical supervision.",
                    "6. IV drips: NAD+, NMN and glutathione under professional guidance.",
                    "7. Hormonal health: assessed and monitored by specialists.",
                    "8. Aesthetic care with the Fotona laser: non-invasive treatments for firmness, radiance and contour.",
                ]),
                ("Fotona treatments we recommend", [
                    "At Impuls Longevity almost 99% of our procedures use Fotona laser technology, a world leader in aesthetics. For anti-ageing we especially recommend:",
                    "Fotona 4D: a non-surgical facial lifting effect without injections, with deep collagen contraction.",
                    "Fotona 4Glow: improves radiance, tone and texture, and treats redness, pores and pigmentation.",
                    "SmoothEye: tightens the eye contour and softens periorbital wrinkles, with very little downtime.",
                    "TightSculpting: firmness and remodelling of the body's skin.",
                    "Fotona technology also offers NightLase (snoring) and IntimaLase (intimate health). Ask our team for the ideal protocol for you.",
                ]),
                ("", ["At Impuls Longevity we focus on natural results and evidence-based treatments. Discuss your plan with our team."]),
            ],
        },
    },
    {
        "slug": "depilacion-laser-cuantas-sesiones",
        "img": "/assets/svc-depilacion-laser.jpg",
        "sources": [
            ("Academia Española de Dermatología y Venereología (AEDV)", "https://aedv.es"),
            ("American Academy of Dermatology (AAD)", "https://www.aad.org"),
            ("Fotona", "https://www.fotona.com"),
        ],
        "es": {
            "title": "Depilación láser: cuántas sesiones necesito y cómo funciona",
            "excerpt": "Cómo actúa el láser sobre el vello, cuántas sesiones suelen hacer falta y cómo preparar la piel en Barcelona.",
            "sections": [
                ("", ["La depilación láser reduce el vello actuando sobre la melanina del folículo durante su fase de crecimiento. Como no todos los folículos crecen a la vez, se necesitan varias sesiones espaciadas para tratar el mayor número posible en fase activa."]),
                ("¿Cuántas sesiones necesito?", ["El número varía según la zona, el tipo y el color del vello, el fototipo de piel y factores hormonales. Como orientación general suelen hacer falta varias sesiones repartidas a lo largo de meses, más algún mantenimiento puntual. La cifra exacta se define en la valoración inicial."]),
                ("Cómo preparar la piel", ["Evita la exposición solar y el autobronceador los días previos, no te depiles con cera ni pinzas (el láser necesita la raíz) y rasura la zona según te indiquemos. Después de la sesión, hidrata la piel y utiliza protección solar."]),
                ("Seguridad y resultados", ["Es un procedimiento seguro cuando lo realiza personal cualificado con un equipo adecuado a tu fototipo. En Impuls Longevity (Barcelona) valoramos tu piel antes de empezar y adaptamos los parámetros del láser Nd:YAG a tu caso."]),
            ],
        },
        "ca": {
            "title": "Depilació làser: quantes sessions necessito i com funciona",
            "excerpt": "Com actua el làser sobre el pèl, quantes sessions solen caldre i com preparar la pell a Barcelona.",
            "sections": [
                ("", ["La depilació làser redueix el pèl actuant sobre la melanina del fol·licle durant la seva fase de creixement. Com que no tots els fol·licles creixen alhora, calen diverses sessions espaiades per tractar el màxim nombre possible en fase activa."]),
                ("Quantes sessions necessito?", ["El nombre varia segons la zona, el tipus i el color del pèl, el fototip de pell i factors hormonals. Com a orientació general solen caldre diverses sessions repartides al llarg de mesos, més algun manteniment puntual. La xifra exacta es defineix a la valoració inicial."]),
                ("Com preparar la pell", ["Evita l'exposició solar i l'autobronzejador els dies previs, no et depilis amb cera ni pinces (el làser necessita l'arrel) i afaita la zona segons t'indiquem. Després de la sessió, hidrata la pell i utilitza protecció solar."]),
                ("Seguretat i resultats", ["És un procediment segur quan el realitza personal qualificat amb un equip adequat al teu fototip. A Impuls Longevity (Barcelona) valorem la teva pell abans de començar i adaptem els paràmetres del làser Nd:YAG al teu cas."]),
            ],
        },
        "ru": {
            "title": "Лазерная депиляция: сколько нужно сеансов и как это работает",
            "excerpt": "Как лазер действует на волос, сколько обычно нужно сеансов и как подготовить кожу.",
            "sections": [
                ("", ["Лазерная депиляция сокращает рост волос, воздействуя на меланин фолликула в фазе роста. Поскольку фолликулы растут не одновременно, нужно несколько сеансов с интервалом, чтобы обработать как можно больше волос в активной фазе."]),
                ("Сколько нужно сеансов?", ["Число зависит от зоны, типа и цвета волос, фототипа кожи и гормональных факторов. Как ориентир — обычно несколько сеансов в течение нескольких месяцев плюс периодическое поддержание. Точную цифру определяем на первой консультации."]),
                ("Как подготовить кожу", ["За несколько дней избегайте солнца и автозагара, не удаляйте волосы воском и пинцетом (лазеру нужен корень), брейте зону по нашим рекомендациям. После сеанса увлажняйте кожу и пользуйтесь солнцезащитой."]),
                ("Безопасность и результат", ["Процедура безопасна, если её выполняет квалифицированный специалист на подходящем вашему фототипу оборудовании. В Impuls Longevity (Барселона) мы оцениваем кожу до начала и настраиваем параметры лазера Nd:YAG под ваш случай."]),
            ],
        },
        "en": {
            "title": "Laser hair removal: how many sessions do I need and how it works",
            "excerpt": "How the laser acts on hair, how many sessions are usually needed and how to prepare your skin.",
            "sections": [
                ("", ["Laser hair removal reduces hair by acting on the follicle's melanin during its growth phase. Because follicles don't grow all at once, several spaced sessions are needed to treat as many active-phase follicles as possible."]),
                ("How many sessions?", ["The number varies with the area, hair type and colour, skin phototype and hormonal factors. As a general guide, several sessions over some months are usually needed, plus occasional maintenance. The exact figure is set at the initial assessment."]),
                ("How to prepare your skin", ["Avoid sun exposure and self-tanner in the days before, don't wax or pluck (the laser needs the root), and shave the area as instructed. After the session, moisturise and use sun protection."]),
                ("Safety and results", ["It is a safe procedure when performed by qualified staff with equipment suited to your phototype. At Impuls Longevity (Barcelona) we assess your skin before starting and tailor the Nd:YAG laser parameters to your case."]),
            ],
        },
    },
    {
        "slug": "eliminar-tatuajes-laser-como-funciona",
        "img": "/assets/svc-eliminacion-de-tatuajes.jpg",
        "sources": [
            ("American Academy of Dermatology (AAD)", "https://www.aad.org"),
            ("U.S. Food & Drug Administration (FDA)", "https://www.fda.gov"),
            ("Fotona", "https://www.fotona.com"),
        ],
        "es": {
            "title": "Aclaración de tatuajes con láser: cómo funciona y qué esperar",
            "excerpt": "Cómo el láser Q-Switched fragmenta la tinta, cuántas sesiones se suelen necesitar y cuidados posteriores.",
            "sections": [
                ("", ["El láser Q-Switched emite pulsos ultracortos de alta energía que fragmentan las partículas de tinta en trozos diminutos. Después, el propio organismo los elimina de forma natural a través del sistema linfático, sesión a sesión."]),
                ("¿Cuántas sesiones?", ["Depende del tamaño, la antigüedad, la profundidad y los colores de la tinta, así como del tipo de piel. Los tatuajes profesionales suelen requerir más sesiones que los amateur. La estimación se realiza en la valoración inicial."]),
                ("Qué esperar y cuidados", ["Entre sesiones se deja un intervalo para que la piel se recupere y el organismo elimine la tinta fragmentada. Es clave proteger la zona del sol y seguir las pautas de cuidado para un mejor resultado y menor riesgo de marcas."]),
                ("Seguridad", ["Debe realizarse siempre por personal cualificado y con valoración previa de la piel. En Impuls Longevity (Barcelona) trabajamos con láser Q-Switched y diseñamos un protocolo personalizado para cada tatuaje."]),
            ],
        },
        "ca": {
            "title": "Aclariment de tatuatges amb làser: com funciona i què esperar",
            "excerpt": "Com el làser Q-Switched fragmenta la tinta, quantes sessions se solen necessitar i cures posteriors.",
            "sections": [
                ("", ["El làser Q-Switched emet polsos ultracurts d'alta energia que fragmenten les partícules de tinta en trossos diminuts. Després, el propi organisme els elimina de manera natural a través del sistema limfàtic, sessió a sessió."]),
                ("Quantes sessions?", ["Depèn de la mida, l'antiguitat, la profunditat i els colors de la tinta, així com del tipus de pell. Els tatuatges professionals solen requerir més sessions que els amateurs. L'estimació es fa a la valoració inicial."]),
                ("Què esperar i cures", ["Entre sessions es deixa un interval perquè la pell es recuperi i l'organisme elimini la tinta fragmentada. És clau protegir la zona del sol i seguir les pautes de cura per a un millor resultat i menor risc de marques."]),
                ("Seguretat", ["S'ha de fer sempre per personal qualificat i amb valoració prèvia de la pell. A Impuls Longevity (Barcelona) treballem amb làser Q-Switched i dissenyem un protocol personalitzat per a cada tatuatge."]),
            ],
        },
        "ru": {
            "title": "Осветление тату лазером: как это работает и чего ожидать",
            "excerpt": "Как лазер Q-Switched дробит пигмент, сколько обычно нужно сеансов и как ухаживать после.",
            "sections": [
                ("", ["Лазер Q-Switched излучает сверхкороткие импульсы высокой энергии, дробящие частицы пигмента на мельчайшие фрагменты. Затем организм сам выводит их естественным образом через лимфатическую систему — сеанс за сеансом."]),
                ("Сколько нужно сеансов?", ["Зависит от размера, давности, глубины и цветов пигмента, а также от типа кожи. Профессиональные татуировки обычно требуют больше сеансов, чем любительские. Оценку делаем на первой консультации."]),
                ("Чего ожидать и уход", ["Между сеансами выдерживают интервал, чтобы кожа восстановилась, а организм вывел раздробленный пигмент. Важно защищать зону от солнца и следовать рекомендациям по уходу — для лучшего результата и меньшего риска следов."]),
                ("Безопасность", ["Процедуру всегда должен выполнять квалифицированный специалист после оценки кожи. В Impuls Longevity (Барселона) мы работаем на лазере Q-Switched и составляем индивидуальный протокол под каждую татуировку."]),
            ],
        },
        "en": {
            "title": "Laser tattoo lightening: how it works and what to expect",
            "excerpt": "How the Q-Switched laser shatters ink, how many sessions are usually needed and aftercare.",
            "sections": [
                ("", ["The Q-Switched laser emits ultra-short, high-energy pulses that break ink particles into tiny fragments. The body then clears them naturally through the lymphatic system, session by session."]),
                ("How many sessions?", ["It depends on the size, age, depth and colours of the ink, as well as your skin type. Professional tattoos usually need more sessions than amateur ones. The estimate is made at the initial assessment."]),
                ("What to expect and aftercare", ["An interval is left between sessions so the skin recovers and the body clears the fragmented ink. Protecting the area from the sun and following aftercare guidance is key for a better result and lower risk of marks."]),
                ("Safety", ["It should always be performed by qualified staff after a skin assessment. At Impuls Longevity (Barcelona) we work with a Q-Switched laser and design a personalised protocol for each tattoo."]),
            ],
        },
    },
]
