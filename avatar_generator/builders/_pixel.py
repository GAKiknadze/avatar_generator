from ._abstract import AbstractAvatarBuilder
from .mixins import OpacityMixin, BackgroundMixin
from PIL import Image, ImageDraw
from .utils import validate_int_param


class PixelAvatarBuilder(OpacityMixin, BackgroundMixin, AbstractAvatarBuilder):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        self._size = validate_int_param(kwargs, 'size', min_value=4, default=256)

    def generate(self, value: int) -> Image:
        """Generate a pixelated avatar from hash value.
        Args:
            value (int): The hash value to generate the avatar from.
        Returns:
            Image: The generated avatar image.
        """
        background_size = self._size
        
        background = self._generate_background(background_size, value)
        
        margin = int(background_size * 0.1)
        image_size = background_size - 2 * margin
        
        size = 8
        scale = image_size // size
        image = Image.new('RGBA', (image_size, image_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        color = (255, 255, 255, self._opacity)

        for y in range(size):
            for x in range((size + 1) // 2):
                idx = x + y * ((size + 1) // 2)
                if (value >> idx) & 1:
                    draw.rectangle(
                        [x * scale, y * scale, (x + 1) * scale, (y + 1) * scale],
                        fill=color
                    )
                    draw.rectangle(
                        [(size - 1 - x) * scale, y * scale, (size - x) * scale, (y + 1) * scale],
                        fill=color
                    )

        background.alpha_composite(image, (margin, margin))
        
        return background
