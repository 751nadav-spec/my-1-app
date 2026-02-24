from PIL import Image, ImageChops

def remove_white_bg(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()
    
    # We will make pixels with a high lightness transparent.
    # To preserve anti-aliased edges, we can map brightness to alpha.
    # 255 (white) -> 0 alpha
    # 0 (black) -> 255 alpha
    
    new_data = []
    for item in datas:
        r, g, b, a = item
        # Calculate brightness
        brightness = (r + g + b) / 3.0
        
        # If the pixel is very close to white (brightness > 240), make it transparent
        if brightness > 250:
            new_data.append((255, 255, 255, 0))
        elif brightness > 200:
            # For anti-aliased edge, fade alpha out
            alpha = int(255 * (255 - brightness) / 55.0)
            # but preserve original RGB so it blends
            new_data.append((r, g, b, alpha))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(out_path, "PNG")

remove_white_bg("logo.png", "logo-transparent.png")
print("Saved transparent logo.")
