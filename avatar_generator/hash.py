from typing import Any
import hashlib
import pickle


def pickle_hash(value: Any) -> int:
    serialized = pickle.dumps(value, protocol=pickle.HIGHEST_PROTOCOL)
    bytes = hashlib.sha256(serialized).digest()
    return int.from_bytes(bytes, 'big')
