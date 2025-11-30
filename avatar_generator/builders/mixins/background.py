from PIL import Image
from ..utils import validate_int_param, validate_bool_param


class BackgroundMixin:
    """Mixin for background generation functionality."""
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        self._background = validate_bool_param(kwargs, 'background', default=True)
        self._max_background_luminance = validate_int_param(kwargs, 'max_background_luminance', min_value=0, max_value=255, default=200)
    
    def _generate_background(self, size: int, value: int) -> Image:
        """Generate a transparent background image.
        Args:
            size (int): The size of the image (width and height).
        Returns:
            Image: The generated transparent background image.
        """
        if not self._background:
            return Image.new('RGBA', (size, size), (0, 0, 0, 0))
        
        max_lum = self._max_background_luminance
        try:
            max_lum = max(0, min(255, int(max_lum)))
        except Exception:
            max_lum = 200

        r = (value >> 16) & 0xFF
        g = (value >> 8) & 0xFF
        b = value & 0xFF

        lum = 0.299 * r + 0.587 * g + 0.114 * b
        if lum > max_lum and lum > 0:
            factor = max_lum / lum
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)

        color = (r, g, b)
        return Image.new('RGBA', (size, size), (*color, 255))

