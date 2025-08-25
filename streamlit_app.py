import streamlit as st
import numpy as np

def generate_histogram(image_data):
    """Generates and displays a pixel intensity histogram for a grayscale image."""

    # Calculate the histogram using NumPy
    histogram = np.zeros(256, dtype=int)
    for pixel_value in image_data.flatten():
        histogram[pixel_value] += 1

    # Display the histogram using Streamlit's chart
    st.bar_chart(histogram)

def main():
    st.title("Pixel Intensity Histogram Generator")

    # Create a sample grayscale image (you can replace this with your own image loading)
    image_data = np.zeros((100, 100), dtype=np.uint8)
    image_data[20:80, 20:80] = 150  # Add a rectangular region with intensity 150
    
    st.write("Displaying a histogram for a sample grayscale image.")

    generate_histogram(image_data)

if __name__ == "__main__":
    main()