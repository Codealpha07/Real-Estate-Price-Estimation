import matplotlib.pyplot as plt # type: ignore
from PIL import Image # type: ignore

# Function to display two images side by side
def display_images_side_by_side(image_path1, image_path2):
    # Load the images using Pillow
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)
    plt.rcParams['figure.figsize'] = (20, 10)
    # Create a figure with 1 row and 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Display the first image
    axes[0].imshow(img1)
    axes[0].set_title('Before', size=15, color="red", weight="bold", pad=15)
    axes[0].axis('off')  # Hide the axis

    # Display the second image
    axes[1].imshow(img2)
    axes[1].set_title('After', size=15, color="red", weight="bold", pad=15)
    axes[1].axis('off')  # Hide the axis

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

# Paths to your images using raw string literals
image_path1 = r'path/to/your/first/image.jpg'
image_path2 = r'path/to/your/second/image.jpg'

# Display the images side by side
display_images_side_by_side(image_path1, image_path2)
