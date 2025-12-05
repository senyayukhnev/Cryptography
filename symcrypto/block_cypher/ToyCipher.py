# для тестов 1.2
from key_schedule import KeyScheduleInterface
from cipher import SymmetricCipherInterface
from typing import List

class ToyKeySchedule(KeyScheduleInterface):
    def expand_key(self, master_key: bytes) -> List[bytes]:
        # For demo: just return the master key repeated as list of round keys
        # In real ciphers you'd produce per-round subkeys
        return [master_key]

class ToyCipher(SymmetricCipherInterface):
    def __init__(self, blocksize: int = 8):
        self._blocksize = blocksize
        self._round_keys: List[bytes] = []

    def expand_key(self, master_key: bytes) -> None:
        # simple "expansion"
        if not isinstance(master_key, (bytes, bytearray)):
            raise TypeError("master_key must be bytes")
        self._round_keys = ToyKeySchedule().expand_key(master_key)

    def encrypt_block(self, block: bytes) -> bytes:
        if len(block) != self._blocksize:
            raise ValueError("block length mismatch")
        # XOR with keystream derived deterministically from round key and block index
        key = self._round_keys[0] if self._round_keys else b'\x00' * self._blocksize
        # derive keystream = key rotated by sum(block bytes) modulo len(key)
        s = sum(block) % max(1, len(key))
        ks = key[s:] + key[:s]
        return bytes([b ^ ks[i % len(ks)] for i, b in enumerate(block)])

    def decrypt_block(self, block: bytes) -> bytes:
        # XOR is symmetric
        return self.encrypt_block(block)

    def block_size(self) -> int:
        return self._blocksize
