import streamlit as st
st.title("StreamLit Select Slider")
st.header("Using the python list to get the values")

options_level = ["level-1","level-2","level-3"]

initilise_slider_variable = st.select_slider("choose a level",options = options_level)
st.write("you just chose : ",initilise_slider_variable)
