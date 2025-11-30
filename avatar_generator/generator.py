from .builders import AbstractAvatarBuilder
from io import BytesIO
from typing import Any, Callable
from PIL import Image
from .hash import pickle_hash


class AvatarGenerator:
    def __init__(self, builder: type[AbstractAvatarBuilder], hash_function: Callable[[Any], int] = pickle_hash, **kwargs) -> None:
        if not issubclass(builder, AbstractAvatarBuilder):
            raise TypeError("builder must be a subclass of AbstractAvatarBuilder")
        
        self._builder = builder(**kwargs)
        self._hash = hash_function

    def _generate(self, value: Any) -> Image:
        object_hash = self._hash(value)
        return self._builder.generate(object_hash)
    
    def save_to_file(self, value: Any, file_path: str) -> None:
        avatar_bytes = self._generate(value)
        avatar_bytes.save(file_path)
    
    def save_to_buffer(self, value: Any, buffer: BytesIO) -> None:
        avatar_bytes = self._generate(value)
        avatar_bytes.save(buffer, format='PNG')
    
    def save_to_bytes(self, value: Any) -> bytes:
        return self._generate(value).tobytes()
