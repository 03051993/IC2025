import streamlit as st

# Título da aplicação
st.title("Inversor de Frases")

# Entrada de texto
frase = st.text_input("Digite uma frase:")

# Botão para inverter a frase
if st.button("Inverter frase"):
    # Verifica se a frase foi preenchida
    if frase:
        # Exibe a frase invertida
        frase_invertida = frase[::-1]
        st.write("Frase invertida:")
        st.write(frase_invertida)
    else:
        st.write("Por favor, digite uma frase para inverter.")

