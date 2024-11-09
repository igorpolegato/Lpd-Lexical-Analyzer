# main.py
from tabulate import tabulate
import sys
from analyzer.analyzer import LexicalAnalyzer, SymbolTable, Token

def main():
    analyser = LexicalAnalyzer()

    if (len(sys.argv)) > 1:
        file_path = sys.argv[1]

    else:
        file_path = input("Digite o caminho do arquivo para análise: ")


    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    tokens = analyser.tokenize(code)

    df = tabulate(tokens, headers=['Token', 'Tipo'], tablefmt="fancy_grid")
    print(df)

if __name__ == "__main__":
    main()
