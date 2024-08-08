import random

ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def nano_id(alphabet: str, size: int) -> str:
    if not isinstance(alphabet, str) or not alphabet:
        raise ValueError("ALPHABET must be a non-empty string")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    
    return ''.join(random.choice(alphabet) for _ in range(size))
