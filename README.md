# Lpd-Lexical-Analyzer

Este repositório contém a implementação de um **analisador léxico** para a linguagem **LPD (Linguagem de Programação Didática)**. Este trabalho foi desenvolvido como parte da avaliação final da disciplina de **Compiladores** no curso de **Engenharia da Computação** da **Universidade de Ribeirão Preto**.

O analisador léxico é um componente fundamental na construção de um **compilador**, responsável pela análise inicial do código-fonte. Ele processa o código de entrada, identifica tokens e seus tipos e fornece as informações necessárias para as etapas subsequentes da compilação.

---

## 📜 Objetivo

O objetivo principal deste projeto é criar um analisador léxico funcional e extensível para a linguagem LPD, que possa ser integrado em um compilador completo.

---

## 🔧 Funcionalidades

### 1. **Reconhecimento de Tokens**
O analisador identifica os seguintes elementos no código-fonte:
- **Palavras Reservadas**
- **Operadores e Delimitadores**
- **Identificadores**
- **Números: Inteiros e de Ponto Flutuante**
- **Literals de Texto**
- **Comentários**

### 2. **Exportação dos Resultados**
Após a análise, os resultados podem ser exportados em:
- **CSV**: Contendo o código-fonte completo e uma tabela com tokens, tipos e linhas.
- **TXT**: Com formato tabular e detalhamento do código analisado.

### 3. **Ignorar Comentários**
O analisador remove automaticamente qualquer comentário delimitado por `{}` antes da análise.

---

## 🛡️ Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 🤝🏼 Contribuidores
- **Igor Polegato** ([GitHub](https://github.com/igorpolegato))
- **Pedro Furtado** ([GitHub](https://github.com/PedroFurtadoC))
