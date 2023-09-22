# 🖥️ Análise de Votações Nominais dos Deputados Brasileiros em 2022

Este trabalho prático foi desenvolvido como parte da disciplina de Algoritmos e Estruturas de Dados III. O objetivo principal era utilizar API's para obter acesso às informações referentes às votações nominais dos deputados brasileiros no ano de 2022.

## API Utilizada

A API utilizada para obter os dados das votações foi a [API de Dados Abertos da Câmara dos Deputados do Brasil](https://dadosabertos.camara.leg.br/). Essa API fornece acesso a uma grande variedade de informações relacionadas às atividades parlamentares.

## Código

O código desenvolvido consiste em uma aplicação Python que faz uso da biblioteca `requests` para consumir a API e manipular os dados obtidos. Abaixo estão destacadas as principais funcionalidades implementadas:

### Classe `Graph`

- **Estrutura de Dados Grafo**: A classe `Graph` foi implementada para representar um grafo direcionado, onde os nós representam os deputados e as arestas indicam votações em comum.

- **Métodos**:
  - `add_node`: Adiciona um nó ao grafo.
  - `add_edge`: Adiciona uma aresta ao grafo, representando uma votação entre dois deputados.
  - `deputies_graph`: Constrói o grafo de deputados utilizando a API, considerando votos favoráveis e contrários.
  - `write_arq`: Armazena os dados do grafo em um arquivo de texto.

### Classe `AmountVotes`

- Essa classe é responsável por armazenar a quantidade de votos de cada deputado.

- **Métodos**:
  - `arquive`: Cria um arquivo que armazena a quantidade de votos de cada deputado.

## Como Executar

Para executar o código, basta ter Python instalado no ambiente e garantir que as bibliotecas `requests` e `json` estejam instaladas. Em seguida, basta rodar o script Python.

## Arquivos Gerados

- `votacaoVotos-2022-graph.txt`: Contém as informações do grafo de deputados, indicando os nós, as arestas e a quantidade de votos em comum.

- `amount-votes-deputies.txt`: Armazena a quantidade de votos de cada deputado.

## Considerações Finais

Este trabalho demonstra a aplicação prática de algoritmos e estruturas de dados na análise de dados parlamentares. A utilização da API da Câmara dos Deputados do Brasil permitiu acesso a informações valiosas e relevantes para a análise política. A construção do grafo de deputados oferece uma representação visual das interações entre os parlamentares nas votações de 2022.

