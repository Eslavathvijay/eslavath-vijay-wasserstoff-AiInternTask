import streamlit as st
import nbformat
from zipfile import ZipFile
from PIL import Image
import os
import io

# Function to display the notebook content
def display_notebook(notebook_file):
    with open(notebook_file, 'r') as f:
        notebook_content = nbformat.read(f, as_version=4)
    for cell in notebook_content.cells:
        if cell.cell_type == 'markdown':
            st.markdown(cell.source)
        elif cell.cell_type == 'code':
            st.code(cell.source)

# Function to extract and display images from a ZIP file
def display_images_from_zip(zip_file):
    with ZipFile(zip_file, 'r') as zip_ref:
        image_files = [f for f in zip_ref.namelist() if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        
        if not image_files:
            st.write("No images found in the ZIP file.")
            return

        for image_name in image_files:
            image_data = zip_ref.read(image_name)
            image = Image.open(io.BytesIO(image_data))
            st.image(image, caption=image_name)

# Streamlit app interface
st.title("Image Object Detection")

# Enter path to the notebook file
notebook_path = st.text_input("C:/Users/eslav/Downloads/VVijay/image-segmentation-and-object-analysis.ipynb")

if notebook_path:
    try:
        st.subheader("Notebook Content")
        display_notebook(notebook_path)
    except FileNotFoundError:
        st.error("File not found. Please check the path and try again.")

# Upload ZIP file containing images
st.subheader("Upload a ZIP file containing images")
uploaded_zip = st.file_uploader("Choose a ZIP file", type="zip")

if uploaded_zip is not None:
    st.subheader("Images from the ZIP file")
    display_images_from_zip(uploaded_zip)