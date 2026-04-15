import streamlit as st 

st.title("Input your Information",anchor=False)
st.divider()

name = st.text_input("Enter your name")

print(type(name))

age = st.number_input("Enter your age",value=None,placeholder="Type your age...")


pressed = st.button("Enter to confirm",type="primary")


selected = st.selectbox("Choose your profession",
             ("Student","Employee","Businessman"),
             index=None,
             accept_new_options = True
             )


print(type(selected))

st.write("You selected " ,selected)





if pressed: 
    st.write(f"Your name is {name} and your age is {age}")









# password = st.text_input("Enter your password",type="password")

# print(type(password))

# st.write("Your password ",password)




