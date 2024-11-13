"""
Módulo de Testes Unitários

Este módulo utiliza o framework `unittest` para realizar testes unitários
nas funcionalidades do analisador léxico (`LexicalAnalyzer`) e da tabela de símbolos (`SymbolTable`).

Os testes incluem:
- Verificação do reconhecimento de palavras reservadas, operadores, delimitadores, números, identificadores e literais de texto.
- Remoção correta de comentários no código fonte.
- Gerenciamento e validação de operações na tabela de símbolos.
- Tratamento de tokens desconhecidos e análise de trechos combinados de código.

Classes:
    - TestLexicalAnalyzer: Testa o funcionamento do analisador léxico.
    - TestSymbolTable: Testa a funcionalidade da tabela de símbolos.
"""

import unittest
import re
from analyzer.analyzer import LexicalAnalyzer, SymbolTable, Token, TokenType


class TestLexicalAnalyzer(unittest.TestCase):
    """
    Classe de Testes para o Analisador Léxico.

    Esta classe implementa métodos de teste para validar a funcionalidade do analisador léxico,
    garantindo o reconhecimento correto de tokens no código fonte.
    """

    def setUp(self):
        """Inicializa o analisador léxico antes de cada teste."""
        self.analyzer = LexicalAnalyzer()

    def test_tokenize_reserved_words(self):
        """Teste: Valida o reconhecimento de palavras reservadas."""
        text = (
            "program begin end var procedure function if then else while do repeat until "
            "char div not or writed writec readc readd int"
        )
        tokens = self.analyzer.tokenize(text)
        expected_types = [
            Token.SPROGRAM, Token.SBEGIN, Token.SEND, Token.SVAR, Token.SPROCEDURE, Token.SFUNCTION,
            Token.SIF, Token.STHEN, Token.SELSE, Token.SWHILE, Token.SDO, Token.SREPEAT, Token.SUNTIL,
            Token.SCHAR, Token.SDIV, Token.SNOT, Token.SOR, Token.SWRITED, Token.SWRITEC,
            Token.SREADC, Token.SREADD, Token.SINT,
        ]
        self.assertEqual([token.type for _, token in tokens], expected_types)

    def test_tokenize_operators_and_delimiters(self):
        """Teste: Valida o reconhecimento de operadores e delimitadores."""
        text = "+ - * / div := < > <= >= == <> ( ) [ ] , ; ."
        tokens = self.analyzer.tokenize(text)
        expected_types = [
            Token.SMAIS, Token.SMENOS, Token.SVEZES, Token.SDIV_FLUTUANTE, Token.SDIV, Token.SATRIBUICAO,
            Token.SMENOR, Token.SMAIOR, Token.SMENOR_IGUAL, Token.SMAIOR_IGUAL, Token.SIGUAL,
            Token.SDIFERENTE, Token.SABRE_PARENTESES, Token.SFECHA_PARENTESES, Token.SABRE_COLCHETE,
            Token.SFECHA_COLCHETE, Token.SVIRGULA, Token.SPONTO_VIRGULA, Token.SPONTO,
        ]
        self.assertEqual([token.type for _, token in tokens], expected_types)

    def test_tokenize_numbers(self):
        """Teste: Valida o reconhecimento de números inteiros e de ponto flutuante."""
        text = "123 45.67 0.99 1000"
        tokens = self.analyzer.tokenize(text)
        expected = [
            ("123", Token.SNUMERO),
            ("45.67", Token.SNUMERO),
            ("0.99", Token.SNUMERO),
            ("1000", Token.SNUMERO),
        ]
        for i, (lexeme, token) in enumerate(tokens):
            self.assertEqual(token.type, expected[i][1], f"Token inesperado: {token.type} para lexema '{lexeme}'")
            self.assertTrue(re.match(r"^\d+(\.\d+)?$", lexeme), f"Formato inválido para número: {lexeme}")

    def test_tokenize_identifiers(self):
        """Teste: Valida o reconhecimento de identificadores."""
        text = "variableName another_var X Y variable123"
        tokens = self.analyzer.tokenize(text)
        for lexeme, token in tokens:
            self.assertEqual(token.type, Token.SIDENTIFICADOR)
            self.assertTrue(re.match(r"^[a-zA-Z_]\w*$", lexeme))

    def test_tokenize_text(self):
        """Teste: Valida o reconhecimento de literais de texto."""
        text = "'A' 'Hello' '123' \"String in quotes\""
        tokens = self.analyzer.tokenize(text)
        expected = [
            ("'A'", Token.STEXTO),
            ("'Hello'", Token.STEXTO),
            ("'123'", Token.STEXTO),
            ("\"String in quotes\"", Token.STEXTO),
        ]
        for i, (lexeme, token) in enumerate(tokens):
            self.assertEqual(token.type, expected[i][1], f"Token inesperado: {token.type} para lexema '{lexeme}'")
            self.assertTrue(re.match(r"^'.*?'|\".*?\"", lexeme), f"Formato inválido para texto: {lexeme}")

    def test_combined_code_snippet(self):
        """Teste: Valida trechos de código combinando palavras reservadas, identificadores e operadores."""
        text = """
        program Example;
        var int A, B;
        A := 10;
        if A > 5 then
            writed(A);
        """
        tokens = self.analyzer.tokenize(text)
        expected_types = [
            Token.SPROGRAM, Token.SIDENTIFICADOR, Token.SPONTO_VIRGULA, Token.SVAR, Token.SINT,
            Token.SIDENTIFICADOR, Token.SVIRGULA, Token.SIDENTIFICADOR, Token.SPONTO_VIRGULA,
            Token.SIDENTIFICADOR, Token.SATRIBUICAO, Token.SNUMERO, Token.SPONTO_VIRGULA, Token.SIF,
            Token.SIDENTIFICADOR, Token.SMAIOR, Token.SNUMERO, Token.STHEN, Token.SWRITED,
            Token.SABRE_PARENTESES, Token.SIDENTIFICADOR, Token.SFECHA_PARENTESES, Token.SPONTO_VIRGULA,
        ]
        self.assertEqual([token.type for _, token in tokens], expected_types)

    def test_tokenize_with_comments(self):
        """Teste: Valida a remoção de comentários no formato `{}`."""
        text = """
        program Test; { This is a comment }
        var int A;
        { Multi-line
          comment }
        A := 10; writed(A);
        """
        tokens = self.analyzer.tokenize(text)
        self.assertNotIn("{", [lexeme for lexeme, _ in tokens])
        self.assertNotIn("}", [lexeme for lexeme, _ in tokens])

    def test_unknown_token(self):
        """Teste: Verifica que tokens desconhecidos não são reconhecidos."""
        text = "@ # $ %"
        tokens = self.analyzer.tokenize(text)
        self.assertTrue(len(tokens) == 0)


class TestSymbolTable(unittest.TestCase):
    """
    Classe de Testes para a Tabela de Símbolos.

    Testa as funcionalidades da `SymbolTable`, garantindo que identificadores sejam gerenciados corretamente.
    """

    def setUp(self):
        """Inicializa a tabela de símbolos antes de cada teste."""
        self.symbol_table = SymbolTable()

    def test_add_and_retrieve_symbols(self):
        """Teste: Adiciona e recupera símbolos da tabela."""
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.add_symbol("var2", Token.SFLOAT)
        self.assertEqual(self.symbol_table.get_symbol("var1"), Token.SINT)
        self.assertEqual(self.symbol_table.get_symbol("var2"), Token.SFLOAT)

    def test_update_existing_symbol(self):
        """Teste: Atualiza o tipo de um símbolo existente."""
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.update_symbol("var1", Token.SFLOAT)
        self.assertEqual(self.symbol_table.get_symbol("var1"), Token.SFLOAT)

    def test_add_duplicate_symbol(self):
        """Teste: Verifica que símbolos duplicados não sobrescrevem os existentes."""
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.add_symbol("var1", Token.SFLOAT)
        self.assertEqual(self.symbol_table.get_symbol("var1"), Token.SINT)

    def test_symbol_not_found(self):
        """Teste: Recupera um símbolo inexistente."""
        result = self.symbol_table.get_symbol("nonexistent")
        self.assertIsNone(result)

    def test_remove_symbol(self):
        """Teste: Remove um símbolo da tabela."""
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.symbols.pop("var1", None)
        self.assertIsNone(self.symbol_table.get_symbol("var1"))

    def test_large_symbol_table(self):
        """Teste: Gerencia uma tabela de símbolos com grande quantidade de entradas."""
        for i in range(1000):
            self.symbol_table.add_symbol(f"var{i}", Token.SINT)
        self.assertEqual(len(self.symbol_table.symbols), 1000)
        self.assertEqual(self.symbol_table.get_symbol("var999"), Token.SINT)


if __name__ == '__main__':
    unittest.main()
