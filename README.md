# AgroLunar - Sistema de Cultivo Hidroponico Autonomo

Projeto da disciplina **Computational Thinking with Python** - FIAP, Engenharia de Software (1o ano).
Global Solution 2026.1 - tema **Industria Espacial**.

## Equipe

| Nome | RM |
|---|---|
| Robert Josino | RM571622 |
| Ryan Maick | RM573051 |
| Vitor Borin | RM573194 |

## Definicao do problema

Levar comida da Terra para a base lunar do programa Artemis custa cerca de US$ 1 milhao
por quilo, e cada astronauta consome perto de 1,8 kg de alimento por dia. Mandar comida
pronta nao se sustenta a longo prazo. Alem disso, a latencia de comunicacao entre a Lua e
a Terra (2,5 segundos) impede controlar uma estufa remotamente em tempo real. E preciso um
sistema que cultive alimento no local e tome decisoes sozinho, sem depender da Terra.

## Solucao

O AgroLunar simula o lado de monitoramento de um sistema de cultivo hidroponico autonomo.
Microcontroladores ESP32 com sensores de temperatura, umidade do ar, umidade do solo e
luminosidade decidem localmente quando ligar a luz e quando regar. Este programa em Python
cadastra camaras de cultivo, le os sensores, calcula o cronograma de iluminacao artificial
com uma funcao cosseno (modelo do ciclo dia/noite) e gera alertas quando um sensor sai da
faixa esperada. A mesma engenharia se aplica a fazendas verticais urbanas na Terra, que
usam 95% menos agua que a agricultura tradicional.

## Como executar

Requer **Python 3.10 ou superior** (necessario para `match-case`). Nao tem dependencia
externa - usa apenas a biblioteca padrao (`os`, `math`, `random`, `datetime`).

```
python agrolunar.py
```

O menu principal aparece com 7 opcoes mais a opcao de sair (0). Apos cada execucao o
programa retorna ao menu inicial.

## Funcionalidades do menu

1. **Cadastrar nova camara de cultivo** (lunar ou urbana) - registra a camara em uma lista.
2. **Consultar status de uma camara** - gera leitura simulada dos 4 sensores e salva no historico.
3. **Calcular cronograma de iluminacao** - usa funcao cosseno para o ciclo de luz (Terra 24h / Lunar 708h).
4. **Gerar alerta de falha** - percorre as leituras e cria alertas quando um sensor sai da faixa.
5. **Listar historico de leituras** - exibe as leituras em tabela formatada.
6. **Sobre o AgroLunar** - descricao da solucao em 5 linhas e dados da equipe.
7. **Catalogo e relatorio da base** - exibe os 4 catalogos da base e calcula estatisticas.
0. **Sair**

## Conceitos de Python aplicados

- **Estruturas de condicao:** `if` / `elif` / `else` e `match-case` (roteador do menu).
- **Estruturas de repeticao:** `while` (loop principal e validacoes) e `for` (percorrer listas).
- **Tratamento de erros:** `try` / `except ValueError` na leitura de numeros (`ler_inteiro`).
- **Subalgoritmos:** funcoes `def` com passagem de parametros e retorno (ex.: `media_lista`, `ler_inteiro`).
- **Listas e strings:** 4 listas de referencia com 20 itens cada (`PLANTAS_HIDROPONICAS`,
  `TEMPERATURAS_HISTORICAS`, `MODULOS_DISPONIVEIS`, `DIAGNOSTICOS_BASE`), alem das listas
  dinamicas `camaras`, `leituras` e `alertas`. Manipulacao de listas feita por funcoes.

## Estrutura do projeto

```
agrolunar.py                 programa principal (codigo-fonte)
descricao_e_execucao.pdf     descricao da solucao e prints de execucao
prints/                      capturas de tela do programa rodando
README.md                    este arquivo
equipe.txt                   integrantes e link do repositorio
```
