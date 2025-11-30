# Avatar Generator

A Python library for generating unique, deterministic pixel-based avatars from hash values. Perfect for creating user profile pictures, identicons, or visual representations based on hashes.

## Overview

Avatar Generator is a flexible and extensible library that transforms hash values into visually distinct avatars. Each hash produces a unique, symmetric pixel pattern with customizable styling options including background colors and opacity levels.

### Features

- **Deterministic Generation**: Same hash always produces the same avatar
- **Customizable Styling**: Control opacity, background colors, and luminance
- **Extensible Architecture**: Easy to add new avatar builders
- **Multiple Export Formats**: Save to file, buffer, or get bytes directly
- **Symmetric Patterns**: Generates aesthetically pleasing mirrored designs

## Installation

```bash
pip install avatar-gen
```

## Quick Start

```python
from avatar_generator import AvatarGenerator, PixelAvatarBuilder

# Generate and save an avatar
AvatarGenerator(builder=PixelAvatarBuilder).save_to_file("user_hash", "avatar.png")
```

## Generator methods

### `save_to_file(hash_value, file_path)`
Generates an avatar from the given hash value and saves it to a file.

**Parameters:**
- `hash_value` (str): The hash or identifier for the avatar
- `file_path` (str): Output path for the generated PNG image

**Example:**
```python
generator = AvatarGenerator(builder=PixelAvatarBuilder)
generator.save_to_file("user123", "avatars/user123.png")
```

### `save_to_buffer(hash_value)`
Generates an avatar and returns it as a BytesIO buffer object.

**Parameters:**
- `hash_value` (str): The hash or identifier for the avatar

**Returns:** `BytesIO` object containing the PNG image data

**Example:**
```python
generator = AvatarGenerator(builder=PixelAvatarBuilder)
buffer = generator.save_to_buffer("user123")
```

### `save_to_bytes(hash_value)`
Generates an avatar and returns the raw bytes of the PNG image.

**Parameters:**
- `hash_value` (str): The hash or identifier for the avatar

**Returns:** `bytes` containing the PNG image data

**Example:**
```python
generator = AvatarGenerator(builder=PixelAvatarBuilder)
image_bytes = generator.save_to_bytes("user123")
```

## Supported avatar builders

- [PixelAvatarBuilder](#pixelavatarbuilder)

### PixelAvatarBuilder

Generates 8x8 pixel-based avatars with symmetric patterns. Each pixel is determined by the hash value, creating unique and recognizable avatars.

#### Parameters

| Parameter | Type | Default | Range | Description |
| - | - | - | - | - |
| `opacity` | int | 200 | 0...255 | Controls the transparency of the white avatar pixels. 0 = fully transparent, 255 = fully opaque. Lower values allow the background to show through. |
| `background` | bool | True | - | Whether to generate a colored background. When True, a unique background color is derived from the hash value. When False, background is transparent. |
| `max_background_luminance` | int | 200 | 0...255 | Maximum brightness level for the background color. Prevents overly bright backgrounds for better contrast with white avatar pixels. Values closer to 0 produce darker backgrounds. |

#### How it works

1. **Avatar Pattern**: The lower 24 bits of the hash determine which pixels are drawn (white color)
2. **Background Color**: The upper 24 bits of the hash determine the background color (RGB values)
3. **Transparency**: The `opacity` parameter controls how transparent the white pixels are, allowing the background to show through
4. **Luminance Control**: The `max_background_luminance` parameter ensures the background isn't too bright, maintaining good contrast

#### Example

```python
from avatar_generator import AvatarGenerator, PixelAvatarBuilder

# Generate with default settings
AvatarGenerator(
    builder=PixelAvatarBuilder
).save_to_file("user123", "avatar.png")

# Generate with custom parameters
AvatarGenerator(
    builder=PixelAvatarBuilder,
    opacity=255,              # Fully opaque pixels
    background=True,          # Include background
    max_background_luminance=150  # Darker backgrounds
).save_to_file("admin@example.com", "admin_avatar.png")

# Generate with semi-transparent effect
AvatarGenerator(
    builder=PixelAvatarBuilder,
    opacity=180,              # 70% opaque
    background=True
).save_to_file("user456", "user456_avatar.png")
```

#### Example Output

![](https://raw.githubusercontent.com/GAKiknadze/avatar_generator/refs/heads/main/docs/images/pixel.png)

## Advanced Usage

### Custom Builder Implementation

You can create custom avatar builders by extending the `AbstractAvatarBuilder` class:

```python
from avatar_generator.builders import AbstractAvatarBuilder
from PIL import Image

class CustomAvatarBuilder(AbstractAvatarBuilder):
    def generate(self, value: int) -> Image:
        # Your custom implementation
        pass
```

### Batch Generation

```python
from avatar_generator import AvatarGenerator, PixelAvatarBuilder

users = ["alice", "bob", "charlie"]
generator = AvatarGenerator(builder=PixelAvatarBuilder)

for user in users:
    generator.save_to_file(user, f"avatars/{user}.png")
```

### Use in Web Applications

```python
from avatar_generator import AvatarGenerator, PixelAvatarBuilder
from io import BytesIO

def get_user_avatar(user_id):
    generator = AvatarGenerator(builder=PixelAvatarBuilder)
    buffer = generator.save_to_buffer(user_id)
    buffer.seek(0)
    return buffer
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See the LICENSE file for details.
