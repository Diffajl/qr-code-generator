import streamlit as st
import qrcode
from PIL import Image
import io

def make_qr(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,  
        border=5    
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

def main():
    st.set_page_config("QR Code Generator | Streamlit")
    st.title("QR Code Generator")

    url_input = st.text_input("Enter URL")

    if url_input:
        buffer = make_qr(url_input)
        
        st.image(buffer, caption="Generated QR Code", use_column_width=True)

        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
