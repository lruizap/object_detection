import os
import shutil

from bing_image_downloader import downloader

# Define the category and total number of images to download
category = "one plastic bottle"  # Search term
total_images = 200               # Number of images to download

# Specify the custom output directory
# Change this to your desired directory name
custom_output_dir = "dataset/plasticBottle"

# Create the directory if it doesn't exist
os.makedirs(custom_output_dir, exist_ok=True)

# Download images into a temporary folder
# Temporary folder for initial downloads
temp_output_dir = "dataset/temp_download"
downloader.download(
    category,                       # Search term
    limit=total_images,             # Number of images to download
    output_dir=temp_output_dir,     # Temporary output directory
    adult_filter_off=True,          # Disable adult content filter
    force_replace=False,            # Do not replace existing images
    timeout=60                      # Timeout for the download
)

# Move downloaded images to the specified output directory
for filename in os.listdir(os.path.join(temp_output_dir, category)):
    src = os.path.join(temp_output_dir, category, filename)
    dst = os.path.join(custom_output_dir, filename)
    shutil.move(src, dst)

# Cleanup: Remove the temporary directory
shutil.rmtree(temp_output_dir)

print(f"Descargadas {total_images} imágenes de {
      category} en la carpeta '{custom_output_dir}'.")
