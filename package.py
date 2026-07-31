#!/usr/bin/env python3
"""Empaqueta el sitio en dist/ para desplegar (Netlify/Cloudflare).

Copia SOLO el sitio generado (html, assets, sitemap.xml, robots.txt),
excluyendo el código fuente Python y archivos de trabajo. Ejecutar
DESPUÉS de build.py.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

# Nombres exactos de carpetas/archivos a excluir del despliegue
EXCLUDE_DIRS = {"dist", "__pycache__", ".git", "programa-perdida-peso"}
EXCLUDE_FILES = {"c.html", "package.py", "build.py", "content.py", "services.py",
                 "pages.py", "legal.py", "blog.py", "privacy.py", ".DS_Store"}


def keep(name, is_dir):
    if is_dir:
        return name not in EXCLUDE_DIRS
    if name in EXCLUDE_FILES:
        return False
    if name.endswith((".py", ".md", ".pyc")):
        return False
    if name.startswith("_") and name.endswith(".html"):  # _measure.html, _mobile.html
        return False
    return True


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    copied = 0
    for base, dirs, files in os.walk(ROOT):
        # podar carpetas excluidas in situ
        dirs[:] = [d for d in dirs if keep(d, True)]
        rel = os.path.relpath(base, ROOT)
        if rel == ".":
            rel = ""
        for f in files:
            if not keep(f, False):
                continue
            src = os.path.join(base, f)
            dst = os.path.join(DIST, rel, f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            copied += 1

    htmls = sum(1 for b, _, fs in os.walk(DIST) for f in fs if f.endswith(".html"))
    print(f"dist/ listo: {copied} archivos ({htmls} .html). Carpeta para desplegar: {DIST}")


if __name__ == "__main__":
    main()
