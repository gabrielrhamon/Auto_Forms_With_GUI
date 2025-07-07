# 🤖 Bot With AutoGui – Automação de Preenchimento de Formulários com PyAutoGUI

Este projeto foi desenvolvido com um objetivo de: **automatizar o preenchimento repetitivo de formulários em uma interface gráfica**, simulando cliques, digitação e navegação com o teclado e mouse como se fosse um usuário real. A ideia é aliviar tarefas maçantes e repetitivas, especialmente em sistemas que não oferecem APIs ou integrações modernas.

## 🧠 O que é o Bot With AutoGui?

O Bot IRIS é um script automatizado baseado em Python que interage diretamente com a tela do computador utilizando a biblioteca `pyautogui`. Ele percorre várias páginas de um sistema, reconhece elementos através de imagens (por meio de `locateOnScreen`) e preenche formulários de forma contextual e lógica, com variações aleatórias para simular comportamento humano. Como se trata de uma solução simples, feita com foco em rapidez e uso individual, não houve a necessidade de criar uma estrutura mais robusta ou generalista. A prioridade foi a funcionalidade direta, que atendesse ao fluxo específico sem complicações.

---

## 📂 Estrutura do Projeto

* `main.py`: Coração do bot. É aqui que os ciclos de preenchimento acontecem, com toda a lógica para validação de página, preenchimento de campos e controle de fluxo.
* `dashboard.py`: Um painel de controle em tempo real no terminal que mostra os ciclos realizados, sucesso, falhas, tempo de execução e a página atual.
* `mouse_c.py`: Ferramenta auxiliar para capturar as coordenadas do mouse em tempo real. Extremamente útil para calibrar os cliques do bot nos locais certos da tela.

---

## ⚙️ Como funciona?

O processo segue uma sequência de **seis páginas** que precisam ser preenchidas em ordem. Em cada etapa, o bot:

1. **Valida visualmente** se está na página certa, usando screenshots de referência.
2. **Executa ações específicas**: clicar, rolar a página, digitar informações aleatórias, selecionar opções, etc.
3. **Atualiza o dashboard** com o status do ciclo.

As informações inseridas incluem:

* Descrições de problemas (como "ausência de sinalização", "material desorganizado", etc.)
* Locais da ocorrência (como "Britagem secundária", "Terramesh"...)
* Classificações ambientais, sociais, materiais, entre outras.

---

## 🎛️ Dashboard em Tempo Real

Durante a execução, um painel no terminal mostra:

* ⏱️ Tempo total de execução
* 🔁 Número total de ciclos
* ✅ Quantos foram bem-sucedidos
* ❌ Quantos falharam (por erro de reconhecimento de página, por exemplo)
* 📍 Página atual em que o bot está
* 🔧 Última ação realizada

É uma forma prática de monitorar o progresso do bot enquanto ele roda.

---

## 🖱️ Como calibrar cliques?

Use o script `mouse_c.py` para descobrir as coordenadas exatas da sua tela:

```bash
python mouse_c.py
```
