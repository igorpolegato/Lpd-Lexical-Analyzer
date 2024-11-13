"""
Módulo `__init__`

Este arquivo inicializa o pacote, facilitando a importação das classes principais do módulo `analyzer`.

O objetivo é expor as funcionalidades centrais para que outros módulos ou pacotes possam utilizar o analisador léxico
e suas classes relacionadas de maneira simplificada.

Classes e Objetos Disponíveis:
    - `LexicalAnalyzer`: Classe responsável por realizar a análise léxica do código-fonte.
    - `SymbolTable`: Classe que implementa a tabela de símbolos para armazenamento e gerenciamento de identificadores.
    - `TokenType`: Classe que representa os diferentes tipos de tokens suportados.
"""

from .analyzer import LexicalAnalyzer, SymbolTable, TokenType
