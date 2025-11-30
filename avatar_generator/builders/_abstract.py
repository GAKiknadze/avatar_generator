from abc import ABC, abstractmethod
from PIL import Image

class AbstractAvatarBuilder(ABC):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @abstractmethod
    def generate(self, value: int) -> Image:
        """Generate an avatar from hash value.
        Args:
            value (int): The hash value to generate the avatar from.
        Returns:
            Image: The generated avatar image.
        """
        raise NotImplementedError("Subclasses must implement this method.")
