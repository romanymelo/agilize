"""Verificação offline da landing page. Uso: py -V:3.12 testes/verificar.py"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
WHATSAPP = ("https://wa.me/5582993079508?text=Ol%C3%A1%21%20Quero%20testar%20o%20"
            "Agilize%20Relat%C3%B3rios%20por%207%20dias.")
PROIBIDAS = ["r$", "preço", "playwright", "supabase", "python"]
LIMITE_IMG = 300 * 1024


class Leitor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []      # (tag, attrs)
        self.texto = []
        self._ignorar = 0

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag in ("script", "style", "head"):
            self._ignorar += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "head"):
            self._ignorar -= 1

    def handle_data(self, data):
        if not self._ignorar:
            self.texto.append(data)


def local(url):
    return url and not re.match(r"^(https?:|mailto:|tel:|#|data:)", url)


def verificar():
    falhas = []
    index = RAIZ / "index.html"
    if not index.exists():
        return ["index.html não encontrado"]
    p = Leitor()
    p.feed(index.read_text(encoding="utf-8"))

    for tag, a in p.tags:
        for attr in ("src", "href"):
            url = a.get(attr)
            if local(url) and not (RAIZ / url.split("#")[0]).exists():
                falhas.append(f"arquivo inexistente: <{tag} {attr}={url}>")

    css = RAIZ / "css" / "style.css"
    if css.exists():
        for url in re.findall(r"url\(['\"]?([^'\")]+)", css.read_text(encoding="utf-8")):
            if local(url) and not (css.parent / url).resolve().exists():
                falhas.append(f"arquivo inexistente no CSS: {url}")

    zap = [a for t, a in p.tags if t == "a" and "wa.me" in a.get("href", "")]
    if not zap:
        falhas.append("nenhum link do WhatsApp")
    for a in zap:
        if a["href"] != WHATSAPP:
            falhas.append(f"link do WhatsApp diferente: {a['href']}")
        if a.get("target") != "_blank":
            falhas.append(f"link do WhatsApp sem target=_blank: {a['href']}")

    texto = " ".join(p.texto).lower()
    for palavra in PROIBIDAS:
        if palavra in texto:
            falhas.append(f"texto proibido na página: {palavra!r}")

    for f in (RAIZ / "img").iterdir():
        if f.stat().st_size > LIMITE_IMG:
            falhas.append(f"imagem acima de 300 KB: {f.name}")

    tem = lambda cond: any(cond(t, a) for t, a in p.tags)
    if not tem(lambda t, a: t == "title"):
        falhas.append("falta <title>")
    if not tem(lambda t, a: t == "meta" and a.get("name") == "description"):
        falhas.append("falta meta description")
    if not tem(lambda t, a: t == "meta" and a.get("property") == "og:image"):
        falhas.append("falta og:image")
    if not tem(lambda t, a: t == "link" and a.get("rel") == "icon"):
        falhas.append("falta link rel=icon")
    return falhas


if __name__ == "__main__":
    falhas = verificar()
    for f in falhas:
        print("FALHA:", f)
    print("OK" if not falhas else f"{len(falhas)} falha(s)")
    sys.exit(1 if falhas else 0)
