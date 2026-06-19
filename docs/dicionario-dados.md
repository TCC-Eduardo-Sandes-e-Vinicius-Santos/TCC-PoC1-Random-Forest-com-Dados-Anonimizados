# Dicionário de Dados

<div align="justify">&emsp;&emsp;
A base de dados 'Cardiovascular Disease Dataset', foi disponibilizada no <a href="https://www.kaggle.com">Kaggle</a> por Svetlana Ulianova, e consiste num conjunto de dados utilizado para tarefas de classificação em Machine Learning. O objetivo principal desta base é prever a presença ou ausência de doenças cardiovasculares em pacientes, com base em informações coletadas no momento de exames médicos.
</div>

<div align="justify">&emsp;&emsp;
Ela contém 70.000 registros de pacientes e 12 atributos (além da variável alvo cardio) e seus dados estão divididos em três categorias principais de recursos, sendo eles:
</div>

1. **Objetivos (Fatuais):** Informações factuais básicas do paciente (idade, altura, peso, gênero).
2. **Exames Médicos:** Resultados de avaliações clínicas (pressão arterial, colesterol, glicose).
3. **Subjetivos:** Informações fornecidas pelo próprio paciente (fumo, consumo de álcool, nível de atividade física).

A base está disponível em: [https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

---

## Diagrama de Dados da Base Original

Abaixo está o dicionário de dados formatado em tabela Markdown com a explicação de cada uma das colunas (variáveis) presentes no dataset:

| Variável        | Tipo de Dado     | Categoria do Recurso | Descrição                                         | Valores / Unidade de Medida                                          |
| --------------- | ---------------- | -------------------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| **id**          | Numérico (Int)   | *N/A*                | Identificador único do paciente.                  | Número inteiro sequencial                                            |
| **age**         | Numérico (Int)   | Objetivo             | Idade do paciente registrada em dias.             | Dias *(Para obter em anos, divide-se por 365,25)*                    |
| **gender**      | Categórico (Int) | Objetivo             | Gênero biológico do paciente.                     | `1` = Mulher<br>`2` = Homem                                          |
| **height**      | Numérico (Int)   | Objetivo             | Altura do paciente.                               | Centímetros (cm)                                                     |
| **weight**      | Numérico (Float) | Objetivo             | Peso do paciente.                                 | Quilogramas (kg)                                                     |
| **ap_hi**       | Numérico (Int)   | Exame Médico         | Pressão arterial sistólica (alta).                | mmHg                                                                 |
| **ap_lo**       | Numérico (Int)   | Exame Médico         | Pressão arterial diastólica (baixa).              | mmHg                                                                 |
| **cholesterol** | Categórico (Int) | Exame Médico         | Nível de colesterol no sangue.                    | `1` = Normal<br>`2` = Acima do normal<br>`3` = Muito acima do normal |
| **gluc**        | Categórico (Int) | Exame Médico         | Nível de glicose (açúcar) no sangue.              | `1` = Normal<br>`2` = Acima do normal<br>`3` = Muito acima do normal |
| **smoke**       | Binário (Int)    | Subjetivo            | Indica se o paciente é fumante.                   | `0` = Não<br>`1` = Sim                                               |
| **alco**        | Binário (Int)    | Subjetivo            | Indica se o paciente consome álcool regularmente. | `0` = Não<br>`1` = Sim                                               |
| **active**      | Binário (Int)    | Subjetivo            | Indica se o paciente pratica atividade física.    | `0` = Não<br>`1` = Sim                                               |
| **cardio**      | Binário (Int)    | **Variável Alvo**    | Indica a presença de doença cardiovascular.       | `0` = Não possui<br>`1` = Possui doença                              |

## Diagrama de Dados da Base Utilizada na PoC1

| Variável        | Tipo de Dado     | Categoria do Recurso | Descrição                                                        | Valores / Unidade de Medida                                          |
| --------------- | ---------------- | -------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| **name**        | Texto (String)   | Dado Pessoal         | Nome completo do titular dos dados.                              | Texto livre contendo nome completo                                   |
| **cpf**         | Numérico (Int)   | Dado Pessoal         | Cadastro de Pessoa Física para identificação única do indivíduo. | 11 dígitos numéricos (CPF brasileiro)                                |
| **id**          | Numérico (Int)   | *N/A*                | Identificador único do paciente.                                 | Número inteiro sequencial                                            |
| **age**         | Numérico (Int)   | Objetivo             | Idade do paciente registrada em dias.                            | Dias *(Para obter em anos, divide-se por 365,25)*                    |
| **gender**      | Categórico (Int) | Objetivo             | Gênero biológico do paciente.                                    | `1` = Mulher<br>`2` = Homem                                          |
| **height**      | Numérico (Int)   | Objetivo             | Altura do paciente.                                              | Centímetros (cm)                                                     |
| **weight**      | Numérico (Float) | Objetivo             | Peso do paciente.                                                | Quilogramas (kg)                                                     |
| **ap_hi**       | Numérico (Int)   | Exame Médico         | Pressão arterial sistólica (alta).                               | mmHg                                                                 |
| **ap_lo**       | Numérico (Int)   | Exame Médico         | Pressão arterial diastólica (baixa).                             | mmHg                                                                 |
| **cholesterol** | Categórico (Int) | Exame Médico         | Nível de colesterol no sangue.                                   | `1` = Normal<br>`2` = Acima do normal<br>`3` = Muito acima do normal |
| **gluc**        | Categórico (Int) | Exame Médico         | Nível de glicose (açúcar) no sangue.                             | `1` = Normal<br>`2` = Acima do normal<br>`3` = Muito acima do normal |
| **smoke**       | Binário (Int)    | Subjetivo            | Indica se o paciente é fumante.                                  | `0` = Não<br>`1` = Sim                                               |
| **alco**        | Binário (Int)    | Subjetivo            | Indica se o paciente consome álcool regularmente.                | `0` = Não<br>`1` = Sim                                               |
| **active**      | Binário (Int)    | Subjetivo            | Indica se o paciente pratica atividade física.                   | `0` = Não<br>`1` = Sim                                               |
| **cardio**      | Binário (Int)    | **Variável Alvo**    | Indica a presença de doença cardiovascular.                      | `0` = Não possui<br>`1` = Possui doença                              |

## Versão

| Versão | Data       | Autor                            | Revisor | Data Revisão |
| ------ | ---------- | -------------------------------- | ------- | ------------ |
| 1.0    | 18/06/2026 | Eduardo Sandes e Vinícius Santos | -       | -            |
|        |            |                                  |         |              |