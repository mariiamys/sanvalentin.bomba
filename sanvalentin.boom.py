import streamlit as st
import random

st.set_page_config(page_title="San Valentín bynotmatcha", page_icon="💘")

# Fondo con CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ff758c, #ff7eb3);
}

h1, h2, h3, p {
    text-align: center;
    color: white;
}

/* Botones */
div.stButton > button {
    background-color: #ff4d6d;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6em 1em;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #e63956;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title(" Feliz San Valentín ")

# Imagen romántica
st.image("bomba.jpeg", use_container_width=True)

st.write("")

# Nombre
nombre = st.text_input("bro y tu nombre?")

st.write("")

col1, col2 = st.columns(2)

with col1:
   if st.button("ns q sí, pero sí"):
    if nombre:
        st.success(f"tmb te quiero, {nombre} 😍")

        st.markdown("""
        <style>
        .explosion {
            animation: explotar 4s ease-out forwards;
            transform: scale(0);
        }

        @keyframes explotar {
            0% {
                transform: scale(0);
                opacity: 0;
            }
            50% {
                transform: scale(1.2);
                opacity: 1;
            }
            75% {
                transform: scale(0.9);
            }
            100% {
                transform: scale(1);
            }
        }
        </style>

        <img src="https://i.pinimg.com/736x/c6/6b/2f/c66b2fd804be0abb7ee7f9b9b7e8bd90.jpg" class="explosion" width="100%">
        """, unsafe_allow_html=True)
    else:
        st.warning("NOMBREEEEE")

import time

with col2:
    if st.button("ns q no, pero no"):
        frases = [
            "OK.",
            "VALE.",
            "BOMBA",
            ]
        st.error(random.choice(frases))

        time.sleep(1)
        st.markdown("""
        <style>
        .explosion {
            animation: explotar 1.2s ease-out forwards;
            transform: scale(0);
        }

        @keyframes explotar {
            0% {
                transform: scale(0);
                opacity: 0;
            }
            50% {
                transform: scale(1.2);
                opacity: 1;
            }
            75% {
                transform: scale(0.9);
            }
            100% {
                transform: scale(1);
            }
        }
        </style>

        <img src="https://i.pinimg.com/736x/56/9a/da/569adaab1867df083984d63db1c5d45a.jpg "  class="explosion" width="100%">
        """, unsafe_allow_html=True)
