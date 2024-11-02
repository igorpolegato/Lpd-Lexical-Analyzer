from typing import Union
import re

class TokenType:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

class Token:
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
        self.lexeme = lexeme
        self.type = ttype
        self.use_regex = use_regex

    def is_(self, tk: Union[str, int]):
        if self.use_regex:
            return re.match(self.lexeme, tk, re.I) is not None

        return self.lexeme == tk

class Analizer:
    def __init__(self) -> None:
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
            Token(r"^[a-z]+[\d\w]*$", Token.SIDENTIFICADOR, use_regex=True),
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
