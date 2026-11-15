# Landing page do Agilize Relatórios — design

Data: 2026-11-14 · Pasta do projeto: `Page/` · Produto: `../V_3` (Agilize Relatórios v3.0)

## Intenção

Uma página única para **contadores e analistas fiscais** de escritórios de contabilidade que atendem empresas na SEFAZ/AL. O objetivo é que o visitante reconheça a dor (emitir relatórios e guias no portal, empresa por empresa, todo mês), veja o programa funcionando e **fale com o Romany pelo WhatsApp para pedir 7 dias de teste**. Se gostar, assina (a assinatura é tratada fora da página).

Sucesso = o visitante clica no botão do WhatsApp.

## Objetivos, não-objetivos e anti-objetivos

- **Objetivos:** deixar claro em segundos o que o programa faz e para quem; mostrar telas reais; levar ao WhatsApp.
- **Não-objetivos:** preço ou planos (não aparecem), formulário, login, download do programa, blog, várias páginas.
- **Anti-objetivos:** parecer genérico ou "template"; jargão técnico de programação (Playwright, Supabase, Python) na página; prometer o que o programa não faz (outros estados, emissão de Certidão).

## Restrições

- Fatos do produto vêm de `../V_3/README.md` e `../V_3/CHANGELOG.md`. Nada inventado.
- Requisitos a declarar: **Windows** e **Google Chrome instalado**; **somente SEFAZ/AL**.
- Imagens usam dados fictícios (já é assim em `../V_3/docs/img`).
- A pasta fica no Google Drive: nada de servidor local nem build; a página tem que abrir com duplo clique no `index.html`.

## Abordagens consideradas

1. **HTML + CSS puro com as imagens numa pasta** — escolhida. Abre direto, zero instalação, hospedagem gratuita em qualquer lugar, ajuste de texto é editar um arquivo.
2. Framework (Astro/Next) — só compensaria com várias páginas ou blog; para uma página é instalação e manutenção à toa.
3. Construtor (Wix/Carrd) — fácil sem código, mas mensalidade para domínio próprio e difícil reproduzir o tema "Lagoa" e o comparativo.

## Decisões do Romany

- **Visual:** tema escuro "Lagoa", o mesmo do programa (direção A).
- **Topo centralizado**, nesta ordem: etiqueta "SEFAZ/AL · para contadores e analistas fiscais" → título "A carteira inteira emitida enquanto você toma um café." → texto de apoio "Malha Fiscal, NF de Entrada, Omissões, Pendências e as guias Antecipado e ST, em lote, a partir de uma planilha." → comparativo **Hoje** (vermelho suave: "login com IE → emitir → salvar PDF → sair → repetir ×50") × **Com o Agilize** (verde: "importar planilha → marcar → Iniciar") → **botão do WhatsApp centralizado** "Testar 7 dias grátis no WhatsApp" → print do programa. **Sem** linha de texto abaixo do botão. O modelo aprovado está em `docs/modelo-topo-aprovado.html` (fragmento de mockup: reproduzir proporções, ordem e cores dele).
- **Contato:** só WhatsApp, `https://wa.me/5582993079508?text=` com a mensagem "Olá! Quero testar o Agilize Relatórios por 7 dias." (URL-encoded).
- **Sem preço** na página.
- **Hospedagem e domínio:** ficam para depois; a página não pode depender de nenhum.

## Estrutura da página (proposta aceita)

1. **Cabeçalho:** logo à esquerda; botão pequeno "Testar grátis" à direita (mesmo link do WhatsApp).
2. **Topo:** como descrito acima. Print: `app-em-execucao.png`.
3. **A dor:** o passo a passo manual do README (abrir o portal, login com IE e senha, Relatórios → Contribuinte, emitir e salvar cada PDF, repetir em outros sistemas, Cobrança DF-e para as guias, sair e recomeçar), fechando com "multiplicado por dezenas de clientes, todo mês".
4. **O que ele emite:** cards — Malha Fiscal (3 relatórios), NF de Entrada (por período), Omissões de entrega, Extrato de Pendências, Guia Antecipado e Guia ST (relatório e DAR separados, por competência ou período).
5. **Como funciona:** 3 passos — importar a planilha (IE, senha, nome) → marcar relatórios e guias → Iniciar. Print da planilha: `planilha-modelo.png`.
6. **Telas reais:** `pasta-resultado.png` (uma pasta por empresa), `resultado-status.png` (planilha de status), `app-lote.png`.
7. **Detalhes que o fiscal valoriza:** guia vencida com escolha da data limite (`guia-vencida.png`); "sem guia" registrada com print da aba contornada (`sem-guia-aba.png`); proteção contra pagar DAR cancelado; erro em uma empresa não para o lote; planilha de status ao final.
8. **Requisitos:** Windows, Google Chrome instalado, somente SEFAZ/AL.
9. **Como funciona o teste:** fala no WhatsApp → recebe acesso por 7 dias → se gostar, assina.
10. **Rodapé:** botão do WhatsApp de novo, logo, "© 2026 Agilize Relatórios".

## Como fica (decisões técnicas — chamadas minhas)

- Arquivos: `Page/index.html`, `Page/css/style.css`, `Page/img/` (cópias das imagens de `../V_3/docs/img` e do logo), `Page/fonts/Rajdhani-Bold.ttf` (copiada de `../V_3`, licença OFL — copiar `OFL.txt` junto).
- Favicon: `../V_3/icone.ico` copiado para `Page/favicon.ico`.
- Logo: `WhatsApp_Image_2026-07-31_at_17.22.46-removebg-preview.png` (fundo transparente) renomeado para `img/logo.png`.
- Cores (do `agilize_v2.3.py`, versão escura): fundo `#040B10`, cards `#08151C`, linhas `#123039`, texto `#E6F4F6`, apoio `#7FA6B2`, verde texto `#3CC9AE`, gradiente do botão `#0C7E6D → #0E7490`, vermelho suave `#F28B82`.
- Fonte: Rajdhani Bold nos títulos (via `@font-face` local); texto corrido em fonte do sistema (Segoe UI / system-ui).
- Responsivo: no celular, o comparativo empilha (Hoje em cima) e os cards viram uma coluna; margem lateral de 16 px, sem rolagem horizontal.
- Sem JavaScript, salvo se algo exigir. Sem bibliotecas externas.
- `<title>`, meta description e Open Graph (imagem: o print do topo) para o link ficar bonito quando compartilhado no WhatsApp. Como ainda não há domínio, `og:image` e `og:url` levam um endereço provisório (`https://SEU-DOMINIO/...`) com um comentário `<!-- TROCAR AO HOSPEDAR -->`; a prévia só funciona depois de publicada (chamada minha).
- Botão do WhatsApp abre em nova aba (`target="_blank" rel="noopener"`).

## Deixado para quem constrói

- Redação final dos textos das seções 3 a 9, fiel ao README, curta e sem jargão de programação.
- Tamanho e compressão das imagens (manter cada uma abaixo de ~300 KB).
- Pequenos ajustes visuais de espaçamento.

## Verificação

- Abrir `index.html` no navegador (desktop e largura de celular) e conferir: topo igual ao modelo aprovado, todas as imagens carregando, links do WhatsApp com o número e a mensagem corretos.
- A prévia do link no WhatsApp fica **fora** desta verificação: só dá para testar depois de hospedar.
- Conferir que nenhum texto menciona preço, outros estados ou Certidão como recurso.

## Atualizações depois da aprovação (2026-11-14 e 2026-11-15)

O que mudou em relação ao desenho acima. Onde houver conflito, vale esta seção.

- **Hospedagem:** saiu do "fica para depois". A página foi ao ar no GitHub Pages e, em seguida, migrou para o **Vercel** (projeto `agilize-relatorios`, ligado ao repositório `romanymelo/agilize`, produção = `main`). O GitHub Pages foi desligado. Endereço: `https://agilize-relatorios.vercel.app/`.
- **Rodapé:** o botão do WhatsApp do rodapé foi retirado (pedido do Romany). Ficam logo e "© 2026 Agilize Relatórios". Os botões do WhatsApp são 3: cabeçalho, topo e final ("Como funciona o teste").
- **Passo 1 do teste:** passou a "Fale conosco no WhatsApp".
- **Prints do programa:** `app-em-execucao.png` e `app-lote.png` tiveram a linha "Desenvolvido por … Contato: …" apagada (pedido do Romany). As originais em `V_3/docs/img` ficam intactas.
- **Fonte:** a Rajdhani deixou de ser carregada de `fonts/Rajdhani-Bold.ttf`, porque o Chrome bloqueia fontes em `file://`. Agora é um subconjunto de 18 KB embutido em base64 no CSS; o TTF foi removido da página, mantendo `fonts/OFL.txt`.
- **Logo:** recortado para tirar a margem transparente (`351×291`, exibido com 60 px de altura).
- **Tags de compartilhamento:** `og:image` e `og:url` usam o endereço do Vercel. A prévia no WhatsApp ainda precisa ser testada.
- **Repositório:** `docs/` e `testes/` agora fazem parte do repositório (não contêm dados sensíveis); `testes/saida/` fica de fora. O `.vercelignore` impede que esses dois sejam publicados no site.
- **Documentação operacional:** ver `README.md`.
