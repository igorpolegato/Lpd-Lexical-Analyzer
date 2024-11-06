# main.py

import sys
from analyzer.analyzer import LexicalAnalyzer, SymbolTable, Token 

def main():
    # Carrega o código-fonte da entrada do usuário ou de um arquivo
    if len(sys.argv) > 1:
        # Se o arquivo foi fornecido como argumento
        with open(sys.argv[1], 'r') as file:
            source_code = file.read()
    else:
        # Solicita o código fonte ao usuário
        source_code = input("Digite o código fonte para análise:\n")

    # Inicializa o analisador léxico e a tabela de símbolos
    analyzer = LexicalAnalyzer()
    symbol_table = SymbolTable()

    # Realiza a análise léxica do código fonte
    tokens = analyzer.tokenize(source_code)

    # Processa e exibe cada token identificado
    print("\nTokens Identificados:")
    for token in tokens:
        print(f"Token: {token.type} - Lexema: {token.lexeme}")

        # Adiciona identificadores à tabela de símbolos
        if token.type == Token.SIDENTIFICADOR:
            symbol_table.add_symbol(token.lexeme, token.type)


    # Exibe a tabela de símbolos
    print("\nTabela de Símbolos:")
    for name, symbol_type in symbol_table.symbols.items():
        print(f"Nome: {name} - Tipo: {symbol_type}")

if __name__ == "__main__":
    main()
