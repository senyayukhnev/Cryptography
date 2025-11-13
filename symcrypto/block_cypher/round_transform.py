from abc import ABC, abstractmethod

class RoundTransformInterface(ABC):
    @abstractmethod
    def transform_block(self, intput_block: bytes, round_key: bytes) -> bytes:
        pass
