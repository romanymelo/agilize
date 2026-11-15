# Landing page do Agilize Relatórios

Página única, em HTML + CSS puro (sem JavaScript, sem build), para contadores e analistas fiscais pedirem **7 dias de teste do Agilize Relatórios pelo WhatsApp**. O produto está em outro repositório; aqui fica só o site.

- **No ar:** https://agilize-relatorios.vercel.app/
- **Repositório:** https://github.com/romanymelo/agilize
- **Hospedagem:** Vercel (projeto `agilize-relatorios`), publicando sozinho a cada `git push` na `main`.

## Estrutura

```
index.html              a página inteira (textos, seções, links)
css/style.css           estilos, cores (variáveis em :root) e regras de celular
img/                    logo e prints do programa (dados fictícios)
fonts/                  rajdhani-sub.woff (fonte dos títulos) e OFL.txt (licença)
favicon.ico             ícone da aba
docs/                   design aprovado, plano de implementação e modelo do topo
testes/verificar.py     confere links, imagens, texto proibido e tamanho das imagens
testes/prints.py        tira prints (computador e celular) e confere rolagem lateral
.vercelignore           mantém docs/ e testes/ fora do site publicado
```

## Atualizar a página (o dia a dia)

1. Edite os arquivos (quase sempre só `index.html` e `css/style.css`).
2. Abra o `index.html` com dois cliques e confira.
3. Rode as verificações (abaixo).
4. Publique:

```bash
git add -A
git commit -m "descreva a mudança"
git push
```

Em cerca de 30 segundos o Vercel publica. Sem etapa de build.

### Onde mexer em cada coisa

| Quero mudar | Onde |
|---|---|
| Texto de uma seção | `index.html`, dentro da `<section>` de mesmo `id`: `dor`, `emite`, `como`, `telas`, `detalhes`, `requisitos`, `teste` |
| Frase do topo, comparativo "Hoje × Com o Agilize" | `<section class="topo">` |
| Número ou mensagem do WhatsApp | O link `https://wa.me/5582993079508?text=...` aparece **3 vezes** no `index.html` (cabeçalho, topo, final). Troque nos 3 e em `WHATSAPP` no `testes/verificar.py`.
| Frases sobre o que o programa faz | Mantenha fiel ao `V_3/README.md`. Pontos que já geraram correção: com a caixa Guia marcada o DAR é **sempre reemitido** (o portal cancela o anterior); o lote **pausa** para perguntar a data de guia vencida; a planilha **exige linha de cabeçalho**; o acesso é de **um computador** por licença | A mensagem vai codificada na URL |
| Cores | Variáveis em `:root` no topo do `css/style.css` (vêm do tema "Lagoa" do programa, versão escura) |
| Layout de celular | Bloco `@media (max-width: 720px)` no fim do `css/style.css` |
| Título, descrição e prévia ao compartilhar | `<head>` do `index.html` (`title`, `description`, `og:*`) |

Regras de conteúdo: sem preço na página; sem jargão técnico (Playwright, Supabase, Python); só SEFAZ/AL; Certidão não é recurso do programa. O `verificar.py` barra preço e jargão.

### Trocar ou atualizar imagens

Os prints vêm de `../V_3/docs/img` (gerados pelo script do programa, com dados fictícios). Ao copiar um novo:

- `app-em-execucao.png` e `app-lote.png` trazem, na base, a linha "Desenvolvido por … Contato: …". Ela foi apagada pintando um retângulo da cor do fundo `(4, 11, 16)` em `(120, 568, 780, 594)`. Refaça isso nos novos (Pillow, `ImageDraw.rectangle`).
- O logo (`img/logo.png`) é o PNG de fundo transparente recortado em `(76, 100, 427, 391)` para tirar a margem.
- Mantenha cada imagem abaixo de 300 KB (o `verificar.py` confere).

### A fonte dos títulos

O Chrome bloqueia fonte carregada por arquivo quando a página é aberta com dois cliques (`file://`). Por isso a Rajdhani Bold está **embutida no CSS em base64**, num subconjunto só com os caracteres do português (18 KB). `fonts/rajdhani-sub.woff` é a mesma fonte, guardada para referência.

Se precisar de um caractere novo, gere outro subconjunto a partir de `../V_3/Rajdhani-Bold.ttf`:

```bash
py -V:3.12 -m pip install fonttools
py -V:3.12 -m fontTools.subset Rajdhani-Bold.ttf --unicodes="U+0020-007E,U+00A0-00FF,U+2013-2014,U+2018-201D,U+2022,U+2026,U+2192,U+00D7" --flavor=woff --output-file=fonts/rajdhani-sub.woff
```

e cole o base64 do `.woff` no `@font-face` do `css/style.css`. A licença é a SIL OFL 1.1 (`fonts/OFL.txt`).

## Verificar

Requisitos: Windows, Python 3.12, `pip install playwright pillow` e Google Chrome instalado.

```bash
py -V:3.12 testes/verificar.py   # esperado: OK
py -V:3.12 testes/prints.py      # esperado: desktop e celular "OK"; prints em testes/saida/
```

Se o `py -V:3.12` não funcionar no seu terminal, use o caminho completo do `python.exe` da instalação 3.12.

O `verificar.py` confere: arquivos referenciados existem; há exatamente 3 links `wa.me`, todos iguais ao oficial, em nova aba e com `rel=noopener`; ausência de preço, jargão, Certidão e do nome e telefone do autor, tanto no texto quanto em `alt`, `title` e `meta`; imagens ≤ 300 KB; e presença de título, descrição, ícone e `og:image` com endereço absoluto (`https://`). Se mudar a quantidade de botões, ajuste `QTD_BOTOES` no script. O `prints.py` falha se houver rolagem lateral em 1366 px ou 375 px.

## Publicar e hospedagem

- O projeto `agilize-relatorios` no Vercel está ligado a este repositório. A `main` é a produção.
- Projeto estático: preset "Other", sem comando de build nem pasta de saída.
- O Vercel ignora `docs/` e `testes/` pelo `.vercelignore` (conferir com `curl -I <site>/docs/`, que deve dar 404).
- Alternativa pela linha de comando: `npx vercel login` e `npx vercel deploy --prod`. A pasta `.vercel/` (vínculo local) não vai para o git.
- O endereço `agilize.vercel.app` pertence a outra pessoa. O nosso é `agilize-relatorios.vercel.app`.
- O GitHub Pages foi desligado; não há hospedagem duplicada.

### Quando houver domínio próprio

1. No Vercel: Project → Settings → Domains → adicionar o domínio e seguir as instruções de DNS.
2. Trocar `og:image` e `og:url` no `<head>` do `index.html` pelo endereço novo (o WhatsApp só mostra a prévia com endereço absoluto) e fazer o push.
3. Atualizar o endereço no topo deste README.

### Prévia no WhatsApp

Depois de qualquer mudança em `og:*` ou na imagem do topo, mande o link para você mesmo no WhatsApp. O WhatsApp guarda a prévia em cache; se não atualizar, tente mais tarde ou acrescente `?v=2` ao link.

## Refazer do zero

O passo a passo completo está em `docs/`:

- `docs/2026-11-14-landing-page-design.md`: intenção, decisões, estrutura da página e o que mudou depois da aprovação.
- `docs/superpowers/plans/2026-11-14-landing-page.md`: as 4 tarefas de implementação, na ordem.
- `docs/modelo-topo-aprovado.html`: o modelo do topo aprovado (fragmento de mockup, não é uma página completa).

## Pendências conhecidas

- Domínio próprio (opcional).
- Texto "Você continua usando sem interrupção" (passo 3 do teste): confirmar que é uma promessa que se quer manter.
- Revisão do código por alguém que não o escreveu ainda não foi feita.

## Licenças

Código da página: uso do autor. Fonte Rajdhani: SIL Open Font License 1.1 (`fonts/OFL.txt`).
