import csv
import os
import sys
from tabulate import tabulate
from analyzer.analyzer import LexicalAnalyzer

def main():
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
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # Extrai o nome base do arquivo (sem extensão)
    file_base_name = os.path.splitext(os.path.basename(file_path))[0]

    tokens = analyser.tokenize(code)

    # Exibe a tabela com o código completo no terminal
    code_table = [(code,)]
    print("\nAnálise do Código Completo:")
    print(tabulate(code_table, headers=["Código LPD"], tablefmt="fancy_grid", stralign="left"))

    # Exibe a tabela com os tokens e tipos no terminal
    token_table = [(lexeme, token.type.name) for lexeme, token in tokens]
    print("\nTokens e Tipos:")
    print(tabulate(token_table, headers=["Tokens", "Tipos"], tablefmt="fancy_grid", stralign="center", colalign=("center", "center")))

    # Pergunta ao usuário se deseja exportar e em qual formato
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
                    # Cabeçalhos das colunas
                    csvwriter.writerow(["Código Completo", "Token", "Tipo"])
                    
                    # Primeira linha com o código completo e células vazias para Token e Tipo
                    csvwriter.writerow([code, "", ""])

                    # Linhas subsequentes com os Tokens e Tipos, sem o código
                    for lexeme, token in tokens:
                        csvwriter.writerow(["", lexeme, token.type.name])

                print(f"\nA análise foi exportada com sucesso para '{os.path.abspath(output_path)}'.")

            elif export_format == 'txt':
                # Exporta para TXT com formatação de tabela
                output_path = f"output-{file_base_name}.txt"
                print("Exportando para TXT...")
                with open(output_path, "w", encoding="utf-8") as txtfile:
                    # Escreve o código completo no início do arquivo
                    txtfile.write("=== Código LPD ===\n")
                    txtfile.write(tabulate(code_table, headers=["Código LPD"], tablefmt="fancy_grid", stralign="left"))
                    txtfile.write("\n\n")
                    txtfile.write("=" * 40 + "\n\n")

                    # Escreve a tabela de Tokens e Tipos
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
