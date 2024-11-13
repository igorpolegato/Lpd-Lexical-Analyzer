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
        self.name = name  # Armazena o nome do tipo do token

    def __str__(self) -> str:
        return self.name  # Retorna o nome do token quando convertido em string

    def __repr__(self) -> str:
        return self.name  # Retorna o nome do token ao imprimir ou representar o objeto

# Define uma classe para representar tokens específicos
class Token:
    """
    Representa um token específico com seu lexema e tipo, incluindo o uso de regex quando necessário.

    Attributes:
        lexeme (str|int): O valor ou padrão do token.
        type (TokenType): O tipo do token, um objeto TokenType.
        use_regex (bool): Indica se o token será identificado por regex.
    """
    # Constantes que representam cada tipo de token, com base nos requisitos e especificações
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
        self.lexeme = lexeme  # Armazena o valor ou padrão do token
        self.type = ttype  # Armazena o tipo do token (um objeto TokenType)
        self.use_regex = use_regex  # Define se o token deve ser identificado por regex

    def is_(self, tk: Union[str, int]):
        """
        Verifica se o lexema do token corresponde ao valor fornecido (tk).

        Args:
            tk (str|int): O valor a ser comparado.

        Returns:
            bool: True se corresponder, False caso contrário.
        """
        if self.use_regex:
            # Se o token usa regex, verifica correspondência usando re.match
            return re.match(self.lexeme, tk, re.I) is not None
        # Se não usa regex, verifica se o lexema é exatamente igual ao valor fornecido
        return self.lexeme == tk

    def __str__(self) -> str:
        return self.type.name

# Define a classe do analisador léxico
class LexicalAnalyzer:
    """
    Responsável por analisar o código fonte, removendo comentários e identificando tokens.

    Attributes:
        tokens (list): Lista de tokens mapeados a lexemas para correspondência durante a análise.
    """
    def __init__(self) -> None:
        # Inicializa a lista de tokens com mapeamento de cada lexema para seu tipo correspondente
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
            # Identificadores são capturados com regex para padrões alfanuméricos
            Token(r"^[a-zA-Z_]\w*$", Token.SIDENTIFICADOR, use_regex=True),
            # Números são capturados com regex para dígitos e pontos decimais
            Token(r"^\d+(\.\d+)?$", Token.SNUMERO, use_regex=True),
            Token(r"\'.{0,1}\'|\".*\"", Token.STEXTO, use_regex=True)
        ]

    def remove_comments(self, text: str) -> str:
        """
        Remove comentários delimitados por `{}` no código de entrada.

        Args:
            text (str): Código fonte de entrada.

        Returns:
            str: Código sem comentários.
        """
        return re.sub(r'\{.*?\}', '', text, flags=re.DOTALL)

    def tokenize(self, text: str) -> list[tuple[Union[str, int], Token]]:
        """
        Realiza a tokenização de uma string de entrada.

        Args:
            text (str): O código fonte a ser analisado.

        Returns:
            list: Lista de tokens identificados.
        """
        tokens = []  # Inicializa a lista de tokens encontrados
        text = self.remove_comments(text)  # Remove comentários do código fonte

        # Divide o texto em tokens usando regex para palavras, operadores e delimitadores
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

        words = re.findall(r"|".join(word_patterns), text)

        for word in words:
            for token in self.tokens:

                if token.is_(word):
                    tokens.append((word, token))
                    break

        return tokens


# Implementação da SymbolTable para armazenar e gerenciar identificadores
class SymbolTable:
    """
    Tabela de símbolos que armazena e gerencia identificadores do código.

    Attributes:
        symbols (dict): Dicionário de símbolos, onde a chave é o nome e o valor é o tipo do símbolo.
    """
    def __init__(self):
        self.symbols = {}  # Inicializa o dicionário de símbolos

    def add_symbol(self, name: str, type: TokenType):
        """
        Adiciona um símbolo à tabela, se ainda não existir.

        Args:
            name (str): Nome do símbolo.
            type (TokenType): Tipo do símbolo.
        """
        if name not in self.symbols:
            self.symbols[name] = type
        else:
            print(f"Warning: Symbol '{name}' already exists.")

    def get_symbol(self, name: str) -> Optional[TokenType]:
        """
        Recupera o tipo de um símbolo armazenado na tabela.

        Args:
            name (str): Nome do símbolo.

        Returns:
            Optional[TokenType]: Tipo do símbolo ou None se não existir.
        """
        return self.symbols.get(name, None)

    def update_symbol(self, name: str, new_type: TokenType):
        """
        Atualiza o tipo de um símbolo existente na tabela.

        Args:
            name (str): Nome do símbolo.
            new_type (TokenType): Novo tipo a ser atribuído ao símbolo.
        """
        if name in self.symbols:
            self.symbols[name] = new_type
        else:
            print(f"Warning: Symbol '{name}' does not exist.")
