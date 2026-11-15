# Landing page do Agilize Relatórios — plano de implementação

> **Para agentes:** SUB-SKILL OBRIGATÓRIA: use superpowers:subagent-driven-development (recomendado) ou superpowers:executing-plans para executar tarefa por tarefa. Os passos usam checkbox (`- [ ]`).

**Objetivo:** uma página estática (`Page/index.html`) que leva contadores e analistas fiscais a pedir 7 dias de teste pelo WhatsApp.

**Arquitetura:** HTML + CSS puro, sem JavaScript e sem bibliotecas externas. Imagens, fonte e favicon copiados para dentro de `Page/`, para a página abrir com duplo clique. A verificação é feita por um script Python (biblioteca padrão) e por um script Playwright que tira prints e mede a rolagem horizontal.

**Stack:** HTML5, CSS (custom properties, grid/flex), Python 3.12 (`py -V:3.12`) com Playwright já instalado (`channel="chrome"`).

> **Nota (2026-11-15):** este plano é o histórico da primeira construção. A seção "Atualizações depois da aprovação" do design e o `README.md` prevalecem (hospedagem no Vercel, fonte embutida em base64 no lugar de `fonts/Rajdhani-Bold.ttf`, 3 botões do WhatsApp, rodapé sem botão).

**Spec:** `Page/docs/2026-11-14-landing-page-design.md` · modelo do topo: `Page/docs/modelo-topo-aprovado.html`

**Git:** o plano foi escrito antes do `git init`; na execução cada tarefa terminou com commit e verificação. Estado atual da hospedagem e do repositório: ver `README.md`.

## Restrições globais

- Caminhos relativos a `Page/`. Origem: `..` = `Agilize Relatorios/`, `../V_3` = produto.
- Link do WhatsApp (todos os botões, idêntico): `https://wa.me/5582993079508?text=Ol%C3%A1%21%20Quero%20testar%20o%20Agilize%20Relat%C3%B3rios%20por%207%20dias.` com `target="_blank" rel="noopener"`.
- Texto do botão principal: `Testar 7 dias grátis no WhatsApp`. Botão do cabeçalho: `Testar grátis`.
- Proibido no texto visível: preço ou `R$`, `Playwright`, `Supabase`, `Python`, outros estados além de Alagoas, Certidão como recurso.
- Cores: `--fundo #040B10`, `--card #08151C`, `--linha #123039`, `--texto #E6F4F6`, `--apoio #7FA6B2`, `--verde #3CC9AE`, `--grad-a #0C7E6D`, `--grad-b #0E7490`, `--vermelho #F28B82`, `--sutil #52808C`.
- Títulos em Rajdhani Bold (`fonts/Rajdhani-Bold.ttf`, `@font-face`); texto em `system-ui, "Segoe UI", sans-serif`.
- Celular: margem lateral de 16 px e nenhuma rolagem horizontal em 375 px.
- Arquivos em UTF-8 sem BOM.

## Foco da revisão

1. Página aberta por `file://` (duplo clique): toda imagem e a fonte precisam carregar por caminho relativo. Coberto pelo `verificar.py` (Tarefa 1).
2. Celular de 375 px: o comparativo e os prints largos não podem estourar a largura. Coberto por `prints.py` (Tarefa 4).
3. Algum botão do WhatsApp com número ou mensagem diferente: todos os `wa.me` precisam ser idênticos ao link oficial. Coberto pelo `verificar.py`.
4. Texto proibido escapando na redação (preço, jargão técnico). Coberto pelo `verificar.py`.
5. Imagens pesadas deixando a página lenta no 4G: nenhuma imagem acima de 300 KB. Coberto pelo `verificar.py`.

---

### Task 1: Assets e script de verificação

**Arquivos:**
- Criar: `img/logo.png` (de `../WhatsApp_Image_2026-07-31_at_17.22.46-removebg-preview.png`)
- Criar: `img/` com cópias de `../V_3/docs/img/`: `app-em-execucao.png`, `app-lote.png`, `planilha-modelo.png`, `pasta-resultado.png`, `resultado-status.png`, `guia-vencida.png`, `sem-guia-aba.png`
- Criar: `fonts/Rajdhani-Bold.ttf` e `fonts/OFL.txt` (de `../V_3/`)
- Criar: `favicon.ico` (de `../V_3/icone.ico`)
- Criar: `testes/verificar.py`

**Interfaces:**
- Produz: `py -V:3.12 testes/verificar.py` → sai com código 0 e imprime `OK` quando tudo passa; senão imprime uma linha `FALHA: ...` por problema e sai com 1.

- [ ] **Passo 1: Copiar os assets** listados acima. Se alguma imagem passar de 300 KB, recomprimir (Pillow, `optimize=True`; se precisar, reduzir para no máximo 1600 px de largura).
- [ ] **Passo 2: Escrever `testes/verificar.py`** usando `html.parser`, sem dependências. Ele lê `index.html` e confere:
  - todo `src`/`href` local (`img`, `link`, `@font-face url(...)` em `css/style.css`) existe em disco;
  - existe pelo menos 1 link `wa.me` e todos são iguais ao link oficial das Restrições globais, com `target="_blank"`;
  - o texto visível não contém (sem diferenciar maiúsculas) `R$`, `preço`, `playwright`, `supabase`, `python`;
  - cada arquivo em `img/` tem ≤ 300 KB;
  - existem `<title>`, `meta[name=description]`, `meta[property=og:image]` e `link[rel=icon]`.
- [ ] **Passo 3: Rodar** `py -V:3.12 testes/verificar.py`. Esperado: `FALHA: index.html não encontrado`, saída 1.

### Task 2: Esqueleto, cabeçalho e topo

**Arquivos:**
- Criar: `index.html`, `css/style.css`

**Interfaces:**
- Consome: assets da Tarefa 1.
- Produz: classes reutilizadas nas Tarefas 3 e 4: `.container` (largura máx. 1080 px), `.secao`, `.titulo-secao`, `.cta` (botão em gradiente), `.card`, `.print` (imagem com borda `--linha` e cantos de 8 px).

- [ ] **Passo 1: `<head>`:** `lang="pt-BR"`, charset, viewport, `<title>Agilize Relatórios — relatórios e guias da SEFAZ/AL em lote</title>`, meta description com o texto de apoio do topo, Open Graph (`og:title`, `og:description`, `og:image` = `https://SEU-DOMINIO/img/app-em-execucao.png`, `og:url` = `https://SEU-DOMINIO/`, ambos marcados com `<!-- TROCAR AO HOSPEDAR -->`) e favicon.
- [ ] **Passo 2: Cabeçalho:** logo à esquerda (altura de cerca de 48 px) e `.cta` pequeno "Testar grátis" à direita.
- [ ] **Passo 3: Topo:** reproduzir `docs/modelo-topo-aprovado.html` (ordem, cores, centralização e textos exatos da spec), com o print `img/app-em-execucao.png` no lugar do placeholder. Sem linha abaixo do botão.
- [ ] **Passo 4: Rodar** `py -V:3.12 testes/verificar.py`. Esperado: `OK`.
- [ ] **Passo 5: Abrir `index.html` no Chrome** e comparar o topo com o modelo aprovado.

### Task 3: Seções 3 a 10

**Arquivos:**
- Modificar: `index.html`, `css/style.css`

**Interfaces:**
- Consome: as classes da Tarefa 2.

Conteúdo de cada seção conforme a spec ("Estrutura da página", itens 3 a 10), com os fatos de `../V_3/README.md`. Títulos de seção (chamada minha, ajustável):

- [ ] **Passo 1:** `#dor` "Todo mês, empresa por empresa" (lista numerada dos 6 passos manuais e fecho "multiplicado por dezenas de clientes, todo mês").
- [ ] **Passo 2:** `#emite` "O que ele emite": 6 `.card` (Malha Fiscal, NF de Entrada, Omissões de entrega, Extrato de Pendências, Guia Antecipado, Guia ST), em grade de 3 colunas.
- [ ] **Passo 3:** `#como` "Como funciona": 3 passos numerados + `img/planilha-modelo.png`.
- [ ] **Passo 4:** `#telas` "O resultado": `pasta-resultado.png`, `resultado-status.png` e `app-lote.png`, com legenda curta.
- [ ] **Passo 5:** `#detalhes` "Pensado para o dia a dia do fiscal": 5 itens; guia vencida com `guia-vencida.png` e sem guia com `sem-guia-aba.png`.
- [ ] **Passo 6:** `#requisitos` com 3 itens: Windows, Google Chrome instalado e somente SEFAZ/AL.
- [ ] **Passo 7:** `#teste` "Como funciona o teste": 3 passos (fala no WhatsApp → 7 dias de acesso → se gostar, assina) + `.cta` principal.
- [ ] **Passo 8:** `<footer>` com logo, `.cta` principal e "© 2026 Agilize Relatórios".
- [ ] **Passo 9: Rodar** `py -V:3.12 testes/verificar.py`. Esperado: `OK`.

### Task 4: Responsivo e prints de conferência

**Arquivos:**
- Modificar: `css/style.css`
- Criar: `testes/prints.py`

**Interfaces:**
- Produz: `py -V:3.12 testes/prints.py` grava `testes/saida/desktop.png` (1366 px) e `testes/saida/celular.png` (375 px, página inteira) e imprime `scrollWidth` × `innerWidth` nas duas larguras. Sai com 1 se `scrollWidth > innerWidth`.

- [ ] **Passo 1: Escrever `testes/prints.py`** com Playwright (`channel="chrome"`, headless), abrindo `index.html` por `file://`.
- [ ] **Passo 2: Rodar.** Esperado antes do CSS responsivo: possível falha em 375 px.
- [ ] **Passo 3: Media query `max-width: 720px`:** comparativo empilhado (Hoje em cima), grades em 1 coluna, `padding-inline: 16px`, imagens com `max-width: 100%`, título do topo menor.
- [ ] **Passo 4: Rodar** `prints.py` e `verificar.py`. Esperado: as duas larguras sem estouro e `OK`. Olhar os dois PNGs.
