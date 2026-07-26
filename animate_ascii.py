import sys
from PIL import Image, ImageDraw, ImageFont

def create_animated_ascii():
    print("Reading ASCII art...")
    with open("face_ascii.txt", "r") as f:
        lines = f.readlines()
        
    # Try to load a nice monospace font (Windows usually has lucon.ttf or consola.ttf)
    try:
        font = ImageFont.truetype("consola.ttf", 12)
    except:
        try:
            font = ImageFont.truetype("lucon.ttf", 12)
        except:
            font = ImageFont.load_default()
            
    print("Calculating image dimensions...")
    # Create a dummy image to calculate text bounding box
    dummy_img = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    full_text = "".join(lines)
    
    # get text dimensions
    if hasattr(draw, "multiline_textbbox"):
        bbox = draw.multiline_textbbox((0, 0), full_text, font=font)
        img_width = bbox[2] + 20
        img_height = bbox[3] + 20
    else:
        # Fallback for older Pillow
        img_width = 800
        img_height = 800

    frames = []
    
    print("Generating frames...")
    # Reveal it line by line (terminal printing effect)
    current_text = ""
    for i in range(len(lines)):
        current_text += lines[i]
        
        # Create a new frame with black background
        frame = Image.new("RGB", (int(img_width), int(img_height)), "black")
        frame_draw = ImageDraw.Draw(frame)
        
        # Draw the current text in Matrix green
        frame_draw.multiline_text((10, 10), current_text, font=font, fill="#00FF41")
        frames.append(frame)
        
    # Add a pause at the end (repeat the last frame 20 times -> 2 seconds)
    print("Finalizing animation...")
    for _ in range(20):
        frames.append(frames[-1])
        
    # Save as GIF
    print("Saving to face_ascii.gif...")
    frames[0].save(
        "face_ascii.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100, # 100 ms per line
        loop=0 # Infinite loop
    )
    print("Success! Saved as face_ascii.gif")

if __name__ == "__main__":
    create_animated_ascii()
