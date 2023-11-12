import streamlit as st

# Title and header for Diwali wishes
st.title(":red[Happy Diwali]")
st.header(":red[Wishing You and Your Family a Very Happy Diwali! Your WellWisher] :blue[ Manish Singh Kashyap]")
st.image("https://media.tenor.com/O7f8mccC-CUAAAAj/happy-diwali-diwali-greeting.gif", caption="Cracker Lights", width="100px", use_column_width=True)

st.snow()

# Button to reveal Diwali gift
btn_click = st.button("Click Here to See Your Gift")

if btn_click:
    st.subheader("🎉 Congratulations! You've Unlocked Your Diwali Gift! 🎁")
    
    # Display balloons animation
    st.balloons()

    # Display cracker lights animation
    st.image("https://media.tenor.com/JehptpXvEbQAAAAd/diwali-diwali-iwshes.gif", width="200px", caption="Lights", use_column_width=True)

    # Display chocolates
    st.image("OIP.jpg", caption="Chocolates", width="200px", use_column_width=True)

    # Display an image with animation

    st.image("photo.jpg", caption="Manish Singh Kashyap", width="100px", use_column_width=True, output_format="auto")
