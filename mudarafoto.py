import streamlit as st
from PIL import Image

def convert_to_black_and_white(image):
    # Converte a imagem para preto e branco
    return image.convert("L")

def main():
    st.title("Conversor de Imagem para Preto e Branco")
    st.write("Faça upload de uma imagem para convertê-la para preto e branco.")

    # Upload da imagem
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg", "bmp"])

    if uploaded_file is not None:
        # Abre a imagem
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem Original", use_column_width=True)

        # Converte para preto e branco
        bw_image = convert_to_black_and_white(image)
        st.image(bw_image, caption="Imagem em Preto e Branco", use_column_width=True)

        # Botão para download da imagem convertida
        bw_image_bytes = bw_image.tobytes()
        bw_image_format = image.format if image.format else "PNG"
        st.download_button(
            label="Baixar Imagem em Preto e Branco",
            data=bw_image.tobytes(),
            file_name=f"imagem_preto_branco.{bw_image_format.lower()}",
            mime=f"image/{bw_image_format.lower()}"
        )

if __name__ == "__main__":
    main()
