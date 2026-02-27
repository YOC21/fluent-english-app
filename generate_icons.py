#!/usr/bin/env python3
"""
Generate PWA icons for FluentEnglish Pro
Creates icons in various sizes required for PWA
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Icon sizes needed for PWA
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

def create_icon(size):
    """Create a beautiful gradient icon with microphone symbol"""
    
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for y in range(size):
        # Purple to pink gradient
        r = int(102 + (118 - 102) * y / size)
        g = int(126 + (75 - 126) * y / size)
        b = int(234 + (162 - 234) * y / size)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    # Add rounded corners mask
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    corner_radius = size // 8
    mask_draw.rounded_rectangle([0, 0, size, size], radius=corner_radius, fill=255)
    
    # Apply mask
    img.putalpha(mask)
    
    # Draw microphone icon
    center_x = size // 2
    center_y = size // 2
    icon_size = int(size * 0.5)
    
    # Microphone body (rounded rectangle)
    body_width = icon_size // 3
    body_height = icon_size // 2
    body_top = center_y - body_height // 2
    body_left = center_x - body_width // 2
    
    draw.rounded_rectangle(
        [body_left, body_top, body_left + body_width, body_top + body_height],
        radius=body_width // 2,
        fill=(255, 255, 255, 230)
    )
    
    # Microphone base (small rectangle)
    base_height = icon_size // 8
    base_width = icon_size // 2
    base_top = body_top + body_height
    base_left = center_x - base_width // 2
    
    draw.rectangle(
        [base_left, base_top, base_left + base_width, base_top + base_height],
        fill=(255, 255, 255, 230)
    )
    
    # Stand (line down)
    stand_height = icon_size // 6
    stand_top = base_top + base_height
    stand_x = center_x
    
    draw.line(
        [(stand_x, stand_top), (stand_x, stand_top + stand_height)],
        fill=(255, 255, 255, 230),
        width=max(2, size // 32)
    )
    
    # Base line
    base_line_width = icon_size // 3
    base_line_y = stand_top + stand_height
    
    draw.line(
        [(center_x - base_line_width//2, base_line_y), 
         (center_x + base_line_width//2, base_line_y)],
        fill=(255, 255, 255, 230),
        width=max(2, size // 32)
    )
    
    return img

def main():
    """Generate all icon sizes"""
    
    # Ensure icons directory exists
    os.makedirs('icons', exist_ok=True)
    
    print("Generating PWA icons...")
    
    for size in ICON_SIZES:
        icon = create_icon(size)
        icon.save(f'icons/icon-{size}x{size}.png', 'PNG')
        print(f"  Created icon-{size}x{size}.png")
    
    print("\nAll icons generated successfully!")
    print("Icons saved in 'icons/' directory")

if __name__ == "__main__":
    main()
