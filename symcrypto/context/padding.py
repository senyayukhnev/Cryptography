from enum import Enum
import secrets


class PaddingEnum(Enum):
    ZEROS = 'zeros'
    ANSI_X923 = 'ansi_x923'
    PKCS7 = 'pkcs7'
    ISO_10126 = 'iso10126'

def pad_zeros(data: bytes, block_size: int) -> bytes:
    pad_len = (-len(data)) % block_size
    if pad_len == 0:
        return data
    return data + b'\x00' * pad_len

def unpad_zeros(data: bytes, block_size: int) -> bytes:
    # ambiguous if original ended with zeros; we remove trailing zeros
    return data.rstrip(b'\x00')

def pad_ansi_x923(data: bytes, block_size: int) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + b'\x00' * (pad_len - 1) + bytes([pad_len])

def unpad_ansi_x923(data: bytes, block_size: int) -> bytes:
    if not data:
        return data
    last = data[-1]
    if not (1 <= last <= block_size):
        raise ValueError("Invalid ANSI X.923 padding")
    if data[-last:-1] != b'\x00' * (last - 1):
        raise ValueError("Invalid ANSI X.923 padding")
    return data[:-last]

def pad_pkcs7(data: bytes, block_size: int) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + bytes([pad_len]) * pad_len

def unpad_pkcs7(data: bytes, block_size: int) -> bytes:
    if not data:
        return data
    last = data[-1]
    if not (1 <= last <= block_size):
        raise ValueError("Invalid PKCS7 padding")
    if data[-last:] != bytes([last]) * last:
        raise ValueError("Invalid PKCS7 padding")
    return data[:-last]

def pad_iso10126(data: bytes, block_size: int) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    rand_bytes = secrets.token_bytes(pad_len - 1) if pad_len > 1 else b''
    return data + rand_bytes + bytes([pad_len])

def unpad_iso10126(data: bytes, block_size: int) -> bytes:
    if not data:
        return data
    last = data[-1]
    if not (1 <= last <= block_size):
        raise ValueError("Invalid ISO10126 padding")
    # cannot validate random bytes, only size
    return data[:-last]

def apply_padding(data: bytes, block_size: int, mode: str) -> bytes:
    if mode == PaddingEnum.ZEROS:
        return pad_zeros(data, block_size)
    if mode == PaddingEnum.ANSI_X923:
        return pad_ansi_x923(data, block_size)
    if mode == PaddingEnum.PKCS7:
        return pad_pkcs7(data, block_size)
    if mode == PaddingEnum.ISO_10126:
        return pad_iso10126(data, block_size)
    raise ValueError("Unknown padding mode")

def remove_padding(data: bytes, block_size: int, mode: str) -> bytes:
    if mode == PaddingEnum.ZEROS:
        return unpad_zeros(data, block_size)
    if mode == PaddingEnum.ANSI_X923:
        return unpad_ansi_x923(data, block_size)
    if mode == PaddingEnum.PKCS7:
        return unpad_pkcs7(data, block_size)
    if mode == PaddingEnum.ISO_10126:
        return unpad_iso10126(data, block_size)
    raise ValueError("Unknown padding mode")
