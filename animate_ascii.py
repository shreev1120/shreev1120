import sys
from PIL import Image, ImageDraw, ImageFont

def create_animated_ascii():
    print("Reading ASCII art...")
    with open("face_ascii.txt", "r") as f:
        # Do not crop to include full height
        lines = f.readlines()
        
    try:
        font = ImageFont.truetype("consola.ttf", 12)
    except:
        try:
            font = ImageFont.truetype("lucon.ttf", 12)
        except:
            font = ImageFont.load_default()
            
    print("Calculating image dimensions...")
    dummy_img = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    full_text = "".join(lines)
    
    if hasattr(draw, "multiline_textbbox"):
        bbox = draw.multiline_textbbox((0, 0), full_text, font=font)
        img_width = bbox[2] + 10  # Reduced padding
        img_height = bbox[3] + 10 # Reduced padding
    else:
        img_width = 800
        img_height = 800

    frames = []
    
    print("Generating frames...")
    current_text = ""
    for i in range(len(lines)):
        current_text += lines[i]
        
        # Use GitHub Dark Mode background color so it blends seamlessly
        frame = Image.new("RGB", (int(img_width), int(img_height)), "#0d1117")
        frame_draw = ImageDraw.Draw(frame)
        
        frame_draw.multiline_text((5, 5), current_text, font=font, fill="#00FF41")
        frames.append(frame)
        
    print("Finalizing animation...")
    for _ in range(20):
        frames.append(frames[-1])
        
    print("Saving to face_ascii.gif...")
    frames[0].save(
        "face_ascii.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    print("Success! Saved as face_ascii.gif")

if __name__ == "__main__":
    create_animated_ascii()
