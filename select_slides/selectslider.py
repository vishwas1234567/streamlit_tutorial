import streamlit as st
st.title("StreamLit Select Slider")
st.header("Using the python list to get the values")

options_level = ["level-1","level-2","level-3"]

initilise_slider_variable = st.select_slider("choose a level",options = options_level)
st.write("you just chose : ",initilise_slider_variable)


st.title("slider -2")

#here we will start workign with the range to selct the data

options_level_range = range(0,100)

initilise_slider_variable_from_range = st.select_slider("choose a level",options = options_level_range)
st.write("you just chose : ",initilise_slider_variable_from_range)
