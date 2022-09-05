from enum import Enum


class TokenTypes(Enum):
    # C language characters
    OPEN_PAR = "("
    CLOSED_PAR = ")"
    OPEN_BRKTS = "{"
    CLOSED_BRKTS = "}"
    SEMI_COLON = ";"
    COMMA = ","
    EOS = "EOS"
    ASSI = "="
    SHARP = "#"
    
    # Arithmetical operators
    SLASH = "/"
    STAR = "*"
    MINUS = "-"
    PLUS = "+"
    MODULO = "%"
    EXCLA = "!"

    # Opé de comparaisons
    GRTR_OR_EQ = ">="
    GRTR = ">"
    LESS = "<"
    LESS_OR_EQ = "<="
    EQUAL = "=="
    DIFF = "!="
    AND = "&&"
    OR = "||"
