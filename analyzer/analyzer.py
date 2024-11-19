"""
Módulo `analyzer`

Este módulo implementa o analisador léxico para a linguagem LPD (Linguagem de Programação Didática).
O analisador léxico é responsável por processar o código-fonte e identificar tokens, seus tipos, 
e estruturas léxicas, fornecendo suporte para análise posterior no processo de compilação.

Classes:
    - TokenType: Representa um tipo genérico de token.
    - Token: Representa um token específico com seu valor (lexema) e tipo.
    - LexicalAnalyzer: Realiza a análise léxica, identificando tokens em código fonte.
    - SymbolTable: Implementa uma tabela de símbolos para gerenciamento de identificadores.
"""

from typing import Union, Optional
import re

# Define um tipo de token, que representa uma categoria de lexemas
class TokenType:
    """
    Representa o tipo de um token, armazenando seu nome.

    Attributes:
        name (str): O nome que descreve o tipo do token.
    """
    def __init__(self, name: str) -> None:
        """
        Inicializa um novo tipo de token.

        Args:
            name (str): O nome que descreve o tipo do token.
        """
        self.name = name

    def __str__(self) -> str:
        """Retorna o nome do tipo do token como string."""
        return self.name  
    
    def __repr__(self) -> str:
        """Retorna a representação textual do tipo do token."""
        return self.name

class Token:
    """
    Representa um token específico com seu lexema e tipo, incluindo o uso de regex.

    Attributes:
        lexeme (str | int): O valor literal ou padrão do token.
        type (TokenType): O tipo do token, representado por um objeto `TokenType`.
        use_regex (bool): Indica se o token deve ser identificado por regex.
    """
    # Define os principais tipos de tokens suportados
    SPROGRAM = TokenType("sprogram")
    SBEGIN = TokenType("sbegin")
    SEND = TokenType("send")
    SPROCEDURE = TokenType("sprocedure")
    SFUNCTION = TokenType("sfunction")
    SIF = TokenType("sif")
    STHEN = TokenType("sthen")
    SELSE = TokenType("selse")
    SWHILE = TokenType("swhile")
    SDO = TokenType("sdo")
    SREPEAT = TokenType("srepeat")
    SUNTIL = TokenType("suntil")
    SATRIBUICAO = TokenType("satribuição")
    SWRITEC = TokenType("swritec")
    SWRITED = TokenType("swrited")
    SREADC = TokenType("sreadc")
    SREADD = TokenType("sreadd")
    SVAR = TokenType("svar")
    SINT = TokenType("sint")
    SFLOAT = TokenType("sfloat")
    SCHAR = TokenType("schar")
    SIDENTIFICADOR = TokenType("sidentificador")
    SNUMERO = TokenType("snúmero")
    SPONTO = TokenType("sponto")
    SPONTO_VIRGULA = TokenType("sponto_virgula")
    SVIRGULA = TokenType("svírgula")
    SABRE_PARENTESES = TokenType("sabre_parênteses")
    SFECHA_PARENTESES = TokenType("sfecha_parênteses")
    SABRE_COLCHETE = TokenType("sabre_colchete")
    SFECHA_COLCHETE = TokenType("sfecha_colchete")
    SAND = TokenType("sand")
    SOR = TokenType("sor")
    SNOT = TokenType("snot")
    SMAIOR = TokenType("smaior")
    SMENOR = TokenType("smenor")
    SIGUAL = TokenType("sigual")
    SDIFERENTE = TokenType("sdiferente")
    SMAIOR_IGUAL = TokenType("smaior_igual")
    SMENOR_IGUAL = TokenType("smenor_igual")
    SMAIS = TokenType("smais")
    SMENOS = TokenType("smenos")
    SVEZES = TokenType("svezes")
    SDIV = TokenType("sdiv")
    SDIV_FLUTUANTE = TokenType("sdiv_flutuante")
    STEXTO = TokenType("stexto")

    def __init__(self, lexeme: Union[str, int], ttype: TokenType, use_regex=False) -> None:
        """
        Inicializa um token específico.

        Args:
            lexeme (str | int): O valor literal ou padrão do token.
            ttype (TokenType): O tipo do token.
            use_regex (bool): Indica se o token será identificado por regex.
        """
        self.lexeme = lexeme
        self.type = ttype
        self.use_regex = use_regex

    def is_(self, tk: Union[str, int]):
        """
        Verifica se o lexema do token corresponde ao valor fornecido.

        Args:
            tk (str | int): O valor a ser comparado.

        Returns:
            bool: `True` se corresponder, `False` caso contrário.
        """
        if self.use_regex:
            return re.match(self.lexeme, tk, re.I) is not None
        return self.lexeme == tk

    def __str__(self) -> str:
        """Retorna o nome do tipo do token."""
        return self.type.name

class LexicalAnalyzer:
    """
    Implementa o analisador léxico para identificar tokens em um código fonte.

    Attributes:
        tokens (list[Token]): Lista de tokens disponíveis para análise.
    """
    def __init__(self) -> None:
        """
        Inicializa o analisador léxico com os tokens suportados.
        """
        self.tokens = [
            Token("and", Token.SAND),
            Token("or", Token.SOR),
            Token("not", Token.SNOT),
            Token("==", Token.SIGUAL),
            Token("<>", Token.SDIFERENTE),
            Token(">=", Token.SMAIOR_IGUAL),
            Token("<=", Token.SMENOR_IGUAL),
            Token(">", Token.SMAIOR),
            Token("<", Token.SMENOR),
            Token("program", Token.SPROGRAM),
            Token("begin", Token.SBEGIN),
            Token("end", Token.SEND),
            Token("procedure", Token.SPROCEDURE),
            Token("function", Token.SFUNCTION),
            Token("if", Token.SIF),
            Token("then", Token.STHEN),
            Token("else", Token.SELSE),
            Token("while", Token.SWHILE),
            Token("do", Token.SDO),
            Token("repeat", Token.SREPEAT),
            Token("until", Token.SUNTIL),
            Token(":=", Token.SATRIBUICAO),
            Token("writec", Token.SWRITEC),
            Token("writed", Token.SWRITED),
            Token("readc", Token.SREADC),
            Token("readd", Token.SREADD),
            Token("var", Token.SVAR),
            Token("int", Token.SINT),
            Token("float", Token.SFLOAT),
            Token("char", Token.SCHAR),
            Token(".", Token.SPONTO),
            Token(";", Token.SPONTO_VIRGULA),
            Token(",", Token.SVIRGULA),
            Token("(", Token.SABRE_PARENTESES),
            Token(")", Token.SFECHA_PARENTESES),
            Token("[", Token.SABRE_COLCHETE),
            Token("]", Token.SFECHA_COLCHETE),
            Token("+", Token.SMAIS),
            Token("-", Token.SMENOS),
            Token("*", Token.SVEZES),
            Token("div", Token.SDIV),
            Token("/", Token.SDIV_FLUTUANTE),

            # Captura identificadores alfanuméricos que começam com uma letra ou sublinhado.
            Token(r"^[a-zA-Z_]\w*$", Token.SIDENTIFICADOR, use_regex=True),
            
            # Captura números inteiros ou de ponto flutuante.
            Token(r"^\d+(\.\d+)?$", Token.SNUMERO, use_regex=True),
            
            # Captura literais de texto delimitados por aspas simples ou duplas.
            Token(r"\'.{0,1}\'|\".*\"", Token.STEXTO, use_regex=True)
        ]

    def remove_comments(self, text: str) -> str:
        """
        Remove comentários no formato `{...}` do código fonte.

        Args:
            text (str): Código fonte de entrada.

        Returns:
            str: Código fonte sem comentários.
        """
        return re.sub(r'\{.*?\}', '', text, flags=re.DOTALL)

    def tokenize(self, text: str) -> list[tuple[Union[str, int], Token, int]]:
        """
        Realiza a análise léxica, identificando tokens no código.

        Args:
            text (str): O código fonte a ser analisado.

        Returns:
            list[tuple[str, Token, int]]: Lista de tokens encontrados com a linha correspondente.
        """
        tokens = []
        text = self.remove_comments(text)
        lines = text.splitlines()

        for line_number, line in enumerate(lines, start=1):
            word_patterns = [
                r"\w+",
                r":=",
                r"<>|[<>]={0,1}",
                r"!=",
                r"==",
                r"\'.{0,1}\'|\".*\"",
                r"/",
                r"[^\s\w]"
            ]
            words = re.findall(r"|".join(word_patterns), line)

            for word in words:
                for token in self.tokens:
                    if token.is_(word):
                        tokens.append((word, token, line_number))
                        break
        return tokens

class SymbolTable:
    """
    Implementa a tabela de símbolos para armazenar e gerenciar identificadores.

    Attributes:
        symbols (dict): Dicionário de símbolos com nome e tipo.
    """
    def __init__(self):
        """Inicializa uma tabela de símbolos."""
        self.symbols = {}

    def add_symbol(self, name: str, type: TokenType):
        """
        Adiciona um símbolo à tabela.

        Args:
            name (str): Nome do símbolo.
            type (TokenType): Tipo do símbolo.
        """
        if name not in self.symbols:
            self.symbols[name] = type
        else:
            print(f"Warning: O Símbolo '{name}' já existe.")

    def get_symbol(self, name: str) -> Optional[TokenType]:
        """
        Recupera o tipo de um símbolo.

        Args:
            name (str): Nome do símbolo.

        Returns:
            Optional[TokenType]: Tipo do símbolo ou `None`.
        """
        return self.symbols.get(name, None)

    def update_symbol(self, name: str, new_type: TokenType):
        """
        Atualiza o tipo de um símbolo na tabela.

        Args:
            name (str): Nome do símbolo.
            new_type (TokenType): Novo tipo do símbolo.
        """
        if name in self.symbols:
            self.symbols[name] = new_type
        else:
            print(f"Warning: O Símbolo '{name}' não existe.")
