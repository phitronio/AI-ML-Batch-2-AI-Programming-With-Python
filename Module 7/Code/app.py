import streamlit as st 
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image



#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")

    #image
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #difficulty 
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    pressed= st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    
    if images and selected_option:

        #note 

        with st.container(border=True):
            st.subheader("Your note")

            #the portion below will be replaced by API Call

            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)





        #Audio transcipt
        with st.container(border=True):
            st.subheader("Audio Transcription")



            #the portion below will be replaced by API Call 
            with st.spinner("AI is generating audio transcript for you"):

                #clearing the markdown

                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")


                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)


        #quiz

        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            #the portion below will be replaced by API Call 

            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)







