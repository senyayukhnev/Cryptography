from enum import Enum

class PaddingEnum(Enum):
    Zeros = 0
    ANSI_X923 = 1
    PKCS7 = 2
    ISO_10126 = 3