from typing import Union
import re

# Define um tipo de token, que representa uma categoria de lexemas
class TokenType:
    def __init__(self, name: str) -> None:
        self.name = name # Armazena o nome do tipo do token


    def __str__(self) -> str:
        return self.name # Retorna o nome do token quando convertido em string

    def __repr__(self) -> str:
        return self.name # Retorna o nome do token ao imprimir ou representar o objeto

# Define uma classe para representar tokens específicos
class Token:
    # Define constantes para cada tipo de token, com seus respectivos nomes
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
    SREPEAT =TokenType("srepeat")
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


    def __init__(self, lexeme: Union[str, int], ttype: TokenType, use_regex=False) -> None:
        self.lexeme = lexeme # Armazena o valor ou padrão do token
        self.type = ttype # Armazena o tipo do token (um objeto TokenType)
        self.use_regex = use_regex # Define se o token deve ser identificado por regex

    def is_(self, tk: Union[str, int]):
        # Verifica se o lexema do token corresponde ao valor fornecido (tk)
        if self.use_regex:
            # Se o token usa regex, verifica correspondência usando re.match
            return re.match(self.lexeme, tk, re.I) is not None
        # Se não usa regex, verifica se o lexema é exatamente igual ao valor fornecido
        return self.lexeme == tk
    
# Define uma classe para o analisador léxico
class Analizer:
    def __init__(self) -> None:
        # Inicializa a lista de tokens, que mapeia cada lexema para seu tipo
        self.tokens = [
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
            # Token para identificadores, usa regex para capturar padrões alfanuméricos
            Token(r"^[a-z]+[\d\w]*$", Token.SIDENTIFICADOR, use_regex=True),
            # Token para números, usa regex para capturar dígitos e pontos decimais
            Token(r"^[0-9.]+$", Token.SNUMERO, use_regex=True),
            Token(".", Token.SPONTO),
            Token(";", Token.SPONTO_VIRGULA),
            Token(",", Token.SVIRGULA),
            Token("(", Token.SABRE_PARENTESES),
            Token(")", Token.SFECHA_PARENTESES),
            Token("[", Token.SABRE_COLCHETE),
            Token("]", Token.SFECHA_COLCHETE),
            Token("and", Token.SAND),
            Token("or", Token.SOR),
            Token("not", Token.SNOT),
            Token(">", Token.SMAIOR),
            Token("<", Token.SMENOR),
            Token("==", Token.SIGUAL),
            Token("!=", Token.SDIFERENTE),
            Token(">=", Token.SMAIOR_IGUAL),
            Token("<=", Token.SMENOR_IGUAL),
            Token("+", Token.SMAIS),
            Token("-", Token.SMENOS),
            Token("*", Token.SVEZES),
            Token("div", Token.SDIV)
        ]
