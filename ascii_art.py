import sys
from PIL import Image

# ASCII characters ordered from darkest to lightest
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    # Console characters are typically twice as tall as they are wide.
    # We multiply by 0.5 to correct the aspect ratio.
    ratio = height / width * 0.5
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    # Map pixel intensity (0-255) to the ASCII_CHARS array
    characters = "".join([ASCII_CHARS[min(pixel//25, len(ASCII_CHARS)-1)] for pixel in pixels])
    return characters

def main(new_width=80):
    path = "my-face.jpeg"
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image file {path}.")
        print(e)
        return
    
    # Process image
    resized = resize_image(image, new_width=new_width)
    gray = grayify(resized)
    new_image_data = pixels_to_ascii(gray)
    
    # Format into a grid
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # Save to file
    with open("face_ascii.txt", "w") as f:
        f.write(ascii_image)
        
    print("Success! Your ASCII face has been saved to face_ascii.txt")

if __name__ == "__main__":
    main()
