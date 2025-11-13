from enum import Enum

class ModeEnum(Enum):
    MODE_ECB = 0
    MODE_CBC = 1
    MODE_PCBC = 2
    MODE_CFB = 3
    MODE_OFB = 4
    MODE_CTR = 5
    MODE_Random_Delta = 6