import os
from PIL import Image

# Function to split an image into 4 equal parts and save them
def split_image(image_path, output_dir):
    with Image.open(image_path) as img:
        width, height = img.size
        # Calculate the size of each part
        part_width = width // 2
        part_height = height // 2
        for i in range(2):
            for j in range(2):
                # Crop the image to get the part
                left = j * part_width
                upper = i * part_height
                right = left + part_width
                lower = upper + part_height
                part = img.crop((left, upper, right, lower))
                # Save the part as a new image
                filename = os.path.splitext(os.path.basename(image_path))[0]
                part_filename = f"{filename}_{i}_{j}.jpg"
                part_path = os.path.join(output_dir, part_filename)
                part.save(part_path)

# Path to the directory containing the images
input_dir = input("enter a filepath: ")
# Path to the directory where the output images will be saved
output_dir = input_dir

# Loop over all the image files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Split the image and save the resulting 4 parts
        image_path = os.path.join(input_dir, filename)
        split_image(image_path, output_dir)
