import unittest
from analyzer.analyzer import LexicalAnalyzer, SymbolTable, Token, TokenType

# Classe de teste para o analisador léxico
class TestLexicalAnalyzer(unittest.TestCase):

    # Configuração inicial antes de cada teste
    def setUp(self):
        # Inicializa uma instância do analisador léxico
        self.analyzer = LexicalAnalyzer()

    # Testa a tokenização de palavras reservadas
    def test_tokenize_reserved_words(self):
        # Entrada com palavras reservadas
        text = "program begin end"
        # Realiza a tokenização
        tokens = self.analyzer.tokenize(text)
        # Verifica se os tokens correspondem aos tipos esperados
        self.assertEqual(tokens[0].type, Token.SPROGRAM)
        self.assertEqual(tokens[1].type, Token.SBEGIN)
        self.assertEqual(tokens[2].type, Token.SEND)

    # Testa a tokenização de identificadores
    def test_tokenize_identifiers(self):
        # Entrada com identificadores
        text = "variableName anotherVar"
        # Realiza a tokenização
        tokens = self.analyzer.tokenize(text)
        # Verifica se os tokens identificados são do tipo 'identificador'
        self.assertEqual(tokens[0].type, Token.SIDENTIFICADOR)
        self.assertEqual(tokens[1].type, Token.SIDENTIFICADOR)

    # Testa a tokenização de números inteiros e de ponto flutuante
    def test_tokenize_numbers(self):
        # Entrada com números
        text = "123 45.67"
        # Realiza a tokenização
        tokens = self.analyzer.tokenize(text)
        # Verifica se os tokens identificados são do tipo 'número'
        self.assertEqual(tokens[0].type, Token.SNUMERO)
        self.assertEqual(tokens[1].type, Token.SNUMERO)

    # Testa o comportamento com tokens desconhecidos
    def test_unknown_token(self):
        # Entrada com um token desconhecido
        text = "@"
        # Realiza a tokenização
        tokens = self.analyzer.tokenize(text)
        # Verifica se nenhum token foi identificado para '@'
        self.assertTrue(len(tokens) == 0)  # Supondo que tokens não reconhecidos são ignorados ou alertados

# Classe de teste para a tabela de símbolos
class TestSymbolTable(unittest.TestCase):

    # Configuração inicial antes de cada teste
    def setUp(self):
        # Inicializa uma instância da tabela de símbolos
        self.symbol_table = SymbolTable()

    # Testa a adição e recuperação de símbolos na tabela
    def test_add_and_get_symbol(self):
        # Adiciona um símbolo à tabela
        self.symbol_table.add_symbol("var1", Token.SINT)
        # Verifica se o símbolo pode ser recuperado corretamente
        self.assertEqual(self.symbol_table.get_symbol("var1"), Token.SINT)

    # Testa a atualização do tipo de um símbolo existente
    def test_update_symbol(self):
        # Adiciona um símbolo e depois atualiza seu tipo
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.update_symbol("var1", Token.SFLOAT)
        # Verifica se o tipo foi atualizado corretamente
        self.assertEqual(self.symbol_table.get_symbol("var1"), Token.SFLOAT)

    # Testa o comportamento ao tentar adicionar um símbolo duplicado
    def test_duplicate_symbol_warning(self):
        # Adiciona um símbolo e tenta adicionar o mesmo símbolo novamente
        self.symbol_table.add_symbol("var1", Token.SINT)
        self.symbol_table.add_symbol("var1", Token.SFLOAT)  # Deve exibir um aviso, mas não substituir o símbolo

# Executa os testes
if __name__ == '__main__':
    unittest.main()
