import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="🖼️ Advanced Image Converter", layout="centered")

# Header
st.markdown("""
    <h2 style="text-align: center;">🖼️ Advanced Image Converter</h2>
    <p style="text-align: center;">Upload → Resize → Compress → Convert → Download 🎯</p>
    <hr>
""", unsafe_allow_html=True)

# Upload
image_file = st.file_uploader("📂 Upload your image", type=["jpg", "jpeg", "png", "webp", "bmp", "tiff", "ico"])

# Supported formats
supported_formats = {
    'JPEG': ['jpg', 'jpeg'],
    'PNG': ['png'],
    'WEBP': ['webp'],
    'BMP': ['bmp'],
    'TIFF': ['tiff'],
    'ICO': ['ico']
}

# Format selection
flat_extensions = [ext for ext_list in supported_formats.values() for ext in ext_list]
selected_format = st.selectbox("🎯 Select output format", flat_extensions)

# Helper: Map extension to PIL format
def get_pil_format(ext):
    for pil_format, extensions in supported_formats.items():
        if ext.lower() in extensions:
            return pil_format
    return None

# Settings Panel
with st.expander("⚙️ Advanced Settings (Optional)", expanded=False):
    resize_option = st.checkbox("Resize Image?")
    width, height = None, None
    if resize_option:
        col1, col2 = st.columns(2)
        with col1:
            width = st.number_input("New Width (px)", min_value=1, step=1)
        with col2:
            height = st.number_input("New Height (px)", min_value=1, step=1)

    compress_option = st.checkbox("Adjust Compression / Quality?")
    quality = 95
    if compress_option:
        quality = st.slider("Select quality (for JPEG/WEBP):", 10, 100, value=85)

# Function to process image
def convert_image(image_file, target_format, resize_dims=None, quality=95):
    img = Image.open(image_file).convert("RGB")
    original_size = img.size

    if resize_dims:
        img = img.resize(resize_dims)

    buffer = BytesIO()
    pil_format = get_pil_format(target_format)

    save_kwargs = {}
    if pil_format in ['JPEG', 'WEBP']:
        save_kwargs['quality'] = quality

    img.save(buffer, format=pil_format, **save_kwargs)
    buffer.seek(0)

    filename = image_file.name.rsplit('.', 1)[0] + '.' + target_format

    st.success("✅ Conversion Successful!")
    st.image(img, caption=f"Preview ({img.size[0]}x{img.size[1]} pixels)", use_container_width=True)
    st.write(f"📏 Original Size: {original_size}, 📐 Final Size: {img.size}")
    st.download_button(
        label="⬇️ Download Image",
        data=buffer,
        file_name=filename,
        mime="image/" + target_format
    )

# Action Trigger
if st.button("🚀 Convert Image"):
    if image_file is not None:
        resize_dims = (int(width), int(height)) if resize_option else None
        convert_image(image_file, selected_format, resize_dims, quality)
    else:
        st.warning("⚠️ Please upload an image first.")
