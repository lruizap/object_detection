import os
import shutil
import random

# Define paths for input and output
input_dir = 'dataset/plasticBottle'
output_train_dir = 'dataset/train'
output_test_dir = 'dataset/test'

# Create output directories if they don't exist
os.makedirs(output_train_dir, exist_ok=True)
os.makedirs(output_test_dir, exist_ok=True)

# Check if the input directory exists
if not os.path.exists(input_dir):
    print(f"Error: El directorio de entrada '{input_dir}' no existe.")
else:
    # List images directly in the input directory
    images = os.listdir(input_dir)

    if len(images) == 0:
        print(f"Advertencia: No se encontraron imágenes en '{input_dir}'.")
    else:
        print(f"Encontradas {len(images)} imágenes en '{input_dir}'.")
        random.shuffle(images)  # Shuffle the images

        # Calculate the number of images for training and testing
        train_size = int(0.8 * len(images))

        # Copy images to the respective output folders with renaming
        for i, image in enumerate(images):
            src_path = os.path.join(input_dir, image)
            if i < train_size:
                dest_path = os.path.join(output_train_dir)
            else:
                dest_path = os.path.join(output_test_dir)

            # Ensure the destination directory exists
            os.makedirs(dest_path, exist_ok=True)

            # Create a new filename with the category name and index
            new_image_name = f"{os.path.basename(input_dir)}_{
                i + 1}.jpg"  # Renaming format
            shutil.copy(src_path, os.path.join(dest_path, new_image_name))

        print(f"Copiadas {train_size} imágenes a entrenamiento y {
              len(images) - train_size} a prueba.")

        shutil.rmtree(input_dir)

print("Imágenes organizadas en conjuntos de entrenamiento y prueba.")
