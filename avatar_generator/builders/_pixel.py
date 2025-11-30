from ._abstract import AbstractAvatarBuilder
from .mixins import OpacityMixin, BackgroundMixin
from PIL import Image, ImageDraw


class PixelAvatarBuilder(OpacityMixin, BackgroundMixin, AbstractAvatarBuilder):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def generate(self, value: int) -> Image:
        """Generate a pixelated avatar from hash value.
        Args:
            value (int): The hash value to generate the avatar from.
        Returns:
            Image: The generated avatar image.
        """
        background_size = 256
        
        background = self._generate_background(background_size, value)
        
        size = 8
        scale = 32
        image_size = size * scale
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

        avatar_offset = (background_size - image_size) // 2
        background.alpha_composite(image, (avatar_offset, avatar_offset))
        
        return background
