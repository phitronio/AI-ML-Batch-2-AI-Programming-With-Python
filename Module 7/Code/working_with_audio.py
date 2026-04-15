from gtts import gTTS
import streamlit as st
import io 

text ="Hello , welcome to this course"


speech = gTTS(text,lang='en',slow=False)



audio_buffer = io.BytesIO()

speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)





