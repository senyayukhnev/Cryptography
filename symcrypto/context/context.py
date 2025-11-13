import asyncio
from typing import Optional
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from symcrypto.block_cypher.cipher import SymmetricCipherInterface
from symcrypto.context.modes_enum import ModeEnum
from symcrypto.context.padding_enum import PaddingEnum


class CryptoContext:
    def __init__(self, cipher_factory, master_key: bytes, mode: ModeEnum, padding: PaddingEnum,
                 iv: Optional[bytes] = None, *, proc_workers: Optional[int] = None,
                 thread_workers: Optional[int] = None, segment_blocks: int = 1024, **mode_params):
        self.cipher_factory = cipher_factory # функция возвращающая уже объект алгоритма шифрования
        self.master_key = master_key
        self.mode = mode
        self.padding = padding
        self.iv: Optional[bytes] = iv
        self.mode_params = mode_params
        self.block_size = cipher_factory().block_size()

        self._local_cipher = cipher_factory()
        self._local_cipher.expand_key(master_key)
        self.loop = asyncio.get_event_loop()
        self._proc_pool = ProcessPoolExecutor(max_workers=proc_workers)
        self._thread_pool = ThreadPoolExecutor(max_workers=thread_workers)
        self._segment_blocks = segment_blocks


    async def encrypt_bytes(self, data: bytes) -> bytes:
        pass

    async def decrypt_bytes(self, data: bytes) -> bytes:
        pass

    async def encrypt_file(self, in_path: str, out_path: str, chunk_size: int = 1 << 20) -> None:
        pass

    async def decrypt_file(self, in_path: str, out_path: str, chunk_size: int = 1 << 20) -> None:
        pass
