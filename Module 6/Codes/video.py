import streamlit as st 

st.title("Input your files (video)",anchor=False)
st.divider()


video_file = st.file_uploader("Enter your audio",
                 type=['mp4','mkv'],
                 )

button = st.button("Click to upload")

if button: 
    if video_file:
        st.video(video_file)
        st.success("Your file is uploaded successfully")
    else:
        st.error("you must upload a file")


