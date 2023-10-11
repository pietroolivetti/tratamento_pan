import streamlit as st
from texts import texts_choice
import pandas as pd
import edge_tts
import subprocess

choice_speed = {'Normal': '--rate=+1%', 'Devagar': '--rate=-25%', 'Rápido': '--rate=+50%'}



with st.sidebar:
    st.title('*Selecione o texto*')
    sel = st.selectbox('Opções de texto:', texts_choice)
    st.divider()
    if len(texts_choice[sel]) > 1:
        st.subheader('Formulários')
        links = [l for l in texts_choice[sel][1:]]
        for d in range(len(links)):
            st.markdown(f"[{links[d][0]}]({links[d][1]})")
        st.divider()
    st.subheader('Para ouvir o texto narrado selecione uma velocidade e clique no botão abaixo')
    selected_speed = st.selectbox('Velocidade: ', choice_speed, index=0)
    if st.button('Ouvir texto'):
        with st.spinner('Convertendo o texto em áudio'):

            subprocess.run(['edge-tts', '--rate=' ,choice_speed[selected_speed] ,'--voice', 'pt-BR-AntonioNeural', '--text', texts_choice[sel][0], '--write-media', 'tts.mp3'])
            st.audio('tts.mp3')
    

st.title(sel)
st.write(texts_choice[sel][0])









