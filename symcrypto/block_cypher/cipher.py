from abc import ABC, abstractmethod

class SymmetricCipherInterface(ABC):
    @abstractmethod
    def set_key(self, key: bytes):
        pass
    @abstractmethod
    def encrypt_block(self, block: bytes) -> bytes:
        pass
    @abstractmethod
    def decrypt_block(self, block: bytes) -> bytes:
        pass
    @abstractmethod
    def block_size(self) -> int:
        pass
