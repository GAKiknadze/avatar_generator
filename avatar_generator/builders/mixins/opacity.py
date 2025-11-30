from ..utils import validate_int_param

class OpacityMixin:
    """Mixin for opacity functionality."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        self._opacity = validate_int_param(kwargs, 'opacity', min_value=0, max_value=255, default=200)
