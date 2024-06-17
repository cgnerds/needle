import numpy as np
from PIL import Image
import os

def create_npz_dataset(images_folder, labels_folder, output_file):
    # Initialize lists to store images and labels
    images = []
    labels = []
    
    # Assuming filenames for images and labels match
    for filename in sorted(os.listdir(images_folder)):
        # Construct full file path
        image_path = os.path.join(images_folder, filename)
        label_path = os.path.join(labels_folder, filename)
        
        # Load image and label
        image = np.array(Image.open(image_path))
        label = np.array(Image.open(label_path))
        
        # Append to lists
        images.append(image)
        labels.append(label)
    
    # Convert lists to NumPy arrays
    images_array = np.array(images)
    labels_array = np.array(labels)
    
    # Save to NPZ file
    np.savez(output_file, arr_0=images_array, arr_1=labels_array)

# Example usage
create_npz_dataset('/path/to/images', '/path/to/labels', 'dataset.npz')