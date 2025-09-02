import streamlit as st
import numpy as np

def create_synthetic_image(width, height):
    """Creates a synthetic image with three distinct intensity peaks."""
    image = np.zeros((height, width), dtype=np.uint8)
    # Simulate air (intensity 30)
    image[image < 50] = 30
    # Simulate soft tissue (intensity 100)
    image[(image >= 50) & (image < 150)] = 100
    # Simulate bone (intensity 200)
    image[image >= 150] = 200
    return image

def calculate_histogram(image):
    """Calculates the pixel intensity histogram using NumPy."""
    # Flatten the image into a 1D array
    pixels = image.flatten()

    # Calculate the histogram using NumPy
    hist, bins = np.histogram(pixels, bins=256, range=[0, 256])

    return hist

def main():
    st.title("Pixel Intensity Histogram App")

    # Create a synthetic image
    width, height = 200, 200
    image = create_synthetic_image(width, height)

    # Calculate the histogram
    histogram_data = calculate_histogram(image)

    # Prepare data for vertical lines with distinct peaks
    air_line = [0] * 30 + [9000] * 5 + [0] * (256 - 35)  # Wider peak for air
    soft_tissue_line = [0] * 100 + [1000] * 5 + [0] * (256 - 105)  # Wider peak for soft tissue
    bone_line = [0] * 200 + [21000] * 5 + [0] * (256 - 205)  # Wider peak for bone

    # Display the histogram with vertical line indicators
    st.line_chart({
        "Air": air_line,
        "Soft Tissue": soft_tissue_line,
        "Bone": bone_line,
    })

if __name__ == "__main__":
    main()