# TCC-PoC1 Random-Forest com Dados Anonimizados

| Aluno                             | Matrícula |
| --------------------------------- | --------- |
| Eduardo Matheus dos Santos Sandes | 221008024 |
| Vinícius de Oliveira Santos       | 202017263 |

Esta Prova de Conceito (PoC) tem como objetivo demonstrar a aplicação do *softgoal* **Anonimização [Dados]**, através das técnicas: **K-Anonimato**, **L-Diversidade** e **T-Proximidade**, visando alcançar **Privacidade [Dados]** em um pipeline de Machine Learning. A PoC avalia o *trade-off* (custo-benefício) entre a proteção dos dados pessoais sensíveis e a precisão (*accuracy*) de um modelo de Inteligência Artificial (Random Forest) treinado para prever doenças cardiovasculares.

<!-- Horkoff -->

## Objetivos da PoC

1. **Injeção de Identificadores Diretos (PII):** Simular uma base de dados real do setor de saúde injetando Nomes e CPFs fictícios em uma base clínica pública.
<!-- 2. **K-Anonimização:** Modelar o Requisito Não-Funcional (NFR) de Privacidade aplicando técnicas de generalização de atributos (idade, peso, altura) e supressão de identificadores (Nome, CPF, ID), garantindo que cada indivíduo seja indistinguível de pelo menos outros *k-1* indivíduos (nesta PoC, $k=5$). -->
2. **Avaliação do *Trade-off* de Utilidade:** Treinar dois modelos de Random Forest, sendo um com os dados exatos (sem privacidade) e outro com os dados anonimizados (com privacidade) e comparar a queda na acurácia preditiva.

3. **Definição de valores ótimos para anonimização nesse contexo:**  Fazer busca em grade sequencial para identificar os limites ideais de **K-Anonimato**, **L-Diversidade** e **T-Proximidade**, visando encontrar o melhor trade-off (custo-benefício) entre a proteção dos dados sensíveis e a acurácia preditiva do modelo de Inteligência Artificial.

## Arquitetura e Fluxo de Dados

O processo está dividido em 4 etapas lineares:

1. **Importação de Dependências:** Carregamento das bibliotecas de manipulação de dados (`pandas`, `numpy`), geração de dados fictícios (`faker`) e modelagem de ML (`scikit-learn`).
2. **Processamento Inicial (`personal_cardio_train.csv`):** - A base pública [Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) é carregada.
* A idade é convertida de dias para anos.
* Nomes (baseados no gênero) e CPFs são gerados via `Faker` e injetados, simulando o vazamento ou exposição de um prontuário médico irrestrito.
3. **Algoritmos de Anonimização (`anonimized_cardio_train.csv`), e**
4. **Treinamento e Relatório:** Pipeline com *One-Hot Encoding* e *Random Forest Classifier* rodando nas duas bases para atestar o custo da privacidade.

---

## Documentação

- [Dicionário de Dados](/docs/dicionario-dados.md)

---

## Estrutura de Diretórios

O repositório segue a seguinte estrutura:

```text
root/
│
├── data/
│   ├── cardio_train.csv             # Dataset original baixado do Kaggle
│   ├── personal_cardio_train.csv    # Gerado pela Etapa 2
│   └── anonimized_cardio_train.csv  # Gerado pela Etapa 3
│
├── docs/
│   └── dicionario-dados.md          # Diagrama dos dados usados na PoC
|
├── src/
│   ├── poc1.ipynb                   # Notebook Jupyter com o código
│   └── poc1_otimizacao.ipynb        # Notebook com a busca em grade dos parâmetros ótimos
│
└── README.md

```

---

## Como Executar

### Opção 1: Rodando no Google Colab

Esta PoC possui uma lógica inteligente de caminhos que se adapta automaticamente ao Google Colab.

1. Baixe o arquivo `cardio_train.csv` no [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset).
2. Abra o [Google Colab](https://colab.research.google.com/) e crie um novo Notebook.
3. Cole o código fornecido nas células do Colab.
4. No menu esquerdo do Colab, clique no ícone de pasta (**Arquivos**).
5. Faça o upload do arquivo `cardio_train.csv` diretamente para a raiz do Colab.
6. Vá em **Ambiente de Execução** > **Executar tudo** (ou execute as células uma a uma).
7. Os arquivos gerados (`personal_cardio_train.csv` e `anonimized_cardio_train.csv`) aparecerão na aba de arquivos do Colab, prontos para download se desejado.

### Opção 2: Rodando Localmente no Computador (PC/Mac)

1. **Pré-requisitos:** Certifique-se de ter o Python 3.8+ instalado.

```bash
# Verificar a versão do Python
python3 --version
```

2. **Crie a estrutura de pastas** conforme o diagrama acima e coloque o `cardio_train.csv` na pasta `data/`.

```bash
git clone https://github.com/TCC-Eduardo-Sandes-e-Vinicius-Santos/TCC-PoC1-Random-Forest-com-Dados-Anonimizados

cd TCC-PoC1-Random-Forest-com-Dados-Anonimizados
```

3. **Abra o terminal** na raiz do projeto e crie um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv

# Para ativar no Windows:
venv\Scripts\activate
# Para ativar no Linux/Mac:
source venv/bin/activate

```


4. **Instale as dependências** executando:
```bash
pip install pandas numpy scikit-learn faker jupyter

```


5. **Inicie o Jupyter Notebook:**
```bash
jupyter notebook

```


6. Abra o arquivo `poc1.ipynb` dentro da pasta `src/` e execute as células. Os arquivos CSV anonimizados serão salvos automaticamente dentro da sua pasta `data/`.

---

## Resultados