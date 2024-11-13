"""
Módulo Principal de Análise Léxica

Este módulo executa a análise léxica de um arquivo fornecido pelo usuário. Ele utiliza o `LexicalAnalyzer` 
para identificar tokens e seus tipos no código fonte, exibindo os resultados de forma organizada no terminal.

Principais funcionalidades:
- Receber e processar um arquivo de código-fonte LPD.
- Realizar a tokenização do código e identificar seus componentes léxicos.
- Exibir o código analisado e os tokens encontrados em formato de tabela no terminal.
- Exportar os resultados da análise em arquivos CSV ou TXT, de acordo com a escolha do usuário.

Dependências:
    - `csv`: Para manipulação e exportação de arquivos CSV.
    - `os`: Para manipulação de caminhos de arquivos.
    - `sys`: Para captura de argumentos de linha de comando.
    - `tabulate`: Para formatação de tabelas no terminal e nos arquivos exportados.
    - `LexicalAnalyzer`: Classe do módulo `analyzer` responsável pela análise léxica.

Funções:
    - main(): Ponto de entrada principal para a execução do analisador.
"""

import csv
import os
import sys
from tabulate import tabulate
from analyzer.analyzer import LexicalAnalyzer

def main():
    """
    Executa a análise léxica em um arquivo de código fornecido pelo usuário.

    Este método solicita o caminho de um arquivo, realiza a análise léxica utilizando
    a classe `LexicalAnalyzer` e exibe os resultados no terminal. Opcionalmente,
    o usuário pode exportar os resultados em formatos CSV ou TXT.

    Etapas:
        1. Solicita o arquivo de entrada.
        2. Verifica a existência e a legibilidade do arquivo.
        3. Processa o código fonte para identificar tokens e seus tipos.
        4. Exibe os resultados em formato tabular no terminal.
        5. Oferece a opção de exportar os resultados em formato CSV ou TXT.
    """
    analyser = LexicalAnalyzer()

    # Solicita o caminho do arquivo a ser analisado
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Digite o caminho do arquivo para análise: ")

    # Verifica se o arquivo existe
    if not os.path.isfile(file_path):
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return

    try:
        # Lê o conteúdo do arquivo
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # Extrai o nome base do arquivo (sem extensão) para uso na exportação
    file_base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Realiza a análise léxica para identificar tokens
    tokens = analyser.tokenize(code)

    # Exibe a tabela com o código completo no terminal
    code_table = [(code,)]
    print("\nAnálise do Código Completo:")
    print(tabulate(code_table, headers=["Código LPD"], tablefmt="fancy_grid", stralign="left"))

    # Exibe a tabela com os tokens e seus tipos
    token_table = [(lexeme, token.type.name) for lexeme, token in tokens]
    print("\nTokens e Tipos:")
    print(tabulate(token_table, headers=["Tokens", "Tipos"], tablefmt="fancy_grid", stralign="center", colalign=("center", "center")))

    # Oferece a opção de exportar os resultados
    export_choice = input("\nDeseja exportar o resultado da análise léxica? (s/n): ").strip().lower()
    if export_choice == 's':
        while True:
            export_format = input("Escolha o formato de exportação (csv/txt): ").strip().lower()
            if export_format in ('csv', 'txt'):
                break
            print("Formato inválido! Por favor, escolha entre 'csv' ou 'txt'.")

        try:
            if export_format == 'csv':
                # Exporta para CSV
                output_path = f"output-{file_base_name}.csv"
                print("Exportando para CSV...")
                with open(output_path, "w", newline='', encoding="utf-8") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # Cabeçalhos
                    csvwriter.writerow(["Código Completo", "Token", "Tipo"])
                    
                    # Primeira linha com o código completo
                    csvwriter.writerow([code, "", ""])

                    # Tokens e seus tipos
                    for lexeme, token in tokens:
                        csvwriter.writerow(["", lexeme, token.type.name])

                print(f"\nA análise foi exportada com sucesso para '{os.path.abspath(output_path)}'.")

            elif export_format == 'txt':
                # Exporta para TXT com formatação tabular
                output_path = f"output-{file_base_name}.txt"
                print("Exportando para TXT...")
                with open(output_path, "w", encoding="utf-8") as txtfile:
                    # Código completo
                    txtfile.write("=== Código LPD ===\n")
                    txtfile.write(tabulate(code_table, headers=["Código LPD"], tablefmt="fancy_grid", stralign="left"))
                    txtfile.write("\n\n")
                    txtfile.write("=" * 40 + "\n\n")

                    # Tokens e seus tipos
                    txtfile.write("=== Tokens e Tipos ===\n")
                    txtfile.write(tabulate(token_table, headers=["Tokens", "Tipos"], tablefmt="fancy_grid", stralign="center", colalign=("center", "center")))
                    txtfile.write("\n")

                print(f"\nA análise foi exportada com sucesso para '{os.path.abspath(output_path)}'.")

        except Exception as e:
            print(f"Erro ao exportar o arquivo: {e}")

    else:
        print("A exportação foi cancelada.")


if __name__ == "__main__":
    main()
