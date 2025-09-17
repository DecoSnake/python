import streamlit as st
import pandas as pd
from datetime import datetime

# CSS para imagem de fundo
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://imgur.com/a/YKRAJvB#WHIaF9y");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Convite de Aniversário", page_icon="🎉")

st.title("🎉 Você está convidado!")
st.markdown("""
Aniversário da Gisele 🎂

📅 Data: 21 de novembro de 2025
🕒 Hora: 15:00
📍 Local: Rua Costa Barros, 1976 – São Paulo/SP

Confirme sua presença abaixo:
""")

nome = st.text_input("Digite seu nome:")
resposta = st.radio("Você vai à festa?", ["Sim", "Não"])
confirmar = st.button("Confirmar Presença")

if confirmar:
    if nome.strip() == "":
        st.warning("Por favor, digite seu nome.")
    else:
        dados = {
            "Nome": nome,
            "Presença": resposta,
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        try:
            df = pd.read_csv("respostas.csv")
            df = df[df["Nome"] != nome]  # Atualiza se já respondeu
            df = pd.concat([df, pd.DataFrame([dados])], ignore_index=True)
        except FileNotFoundError:
            df = pd.DataFrame([dados])

        df.to_csv("respostas.csv", index=False)
        st.success("Obrigado pela confirmação! 🎉")


with st.expander("Ver confirmações"):
    try:
        df = pd.read_csv("respostas.csv")
        st.dataframe(df)
    except:
        st.write("Nenhuma confirmação ainda.")
