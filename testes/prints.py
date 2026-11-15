"""Prints de conferência e checagem de rolagem horizontal. Uso: py -V:3.12 testes/prints.py"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "testes" / "saida"
LARGURAS = {"desktop": 1366, "celular": 375}


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    falhou = False
    with sync_playwright() as p:
        navegador = p.chromium.launch(channel="chrome")
        for nome, largura in LARGURAS.items():
            pagina = navegador.new_page(viewport={"width": largura, "height": 900})
            pagina.goto((RAIZ / "index.html").as_uri())
            for _ in range(25):  # rola para carregar as imagens com loading=lazy
                pagina.mouse.wheel(0, 800)
                pagina.wait_for_timeout(80)
            pagina.wait_for_timeout(400)
            scroll, inner = pagina.evaluate(
                "[document.documentElement.scrollWidth, window.innerWidth]")
            ok = scroll <= inner
            falhou |= not ok
            print(f"{nome}: scrollWidth={scroll} innerWidth={inner} {'OK' if ok else 'FALHA'}")
            pagina.screenshot(path=str(SAIDA / f"{nome}.png"), full_page=True)
            pagina.close()
        navegador.close()
    sys.exit(1 if falhou else 0)


if __name__ == "__main__":
    main()
