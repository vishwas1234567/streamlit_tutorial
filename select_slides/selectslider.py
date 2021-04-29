import streamlit as st
st.title("StreamLit Select Slider")
st.header("Using the python list to get the values")

options_level = ["level-1","level-2","level-3"]
st.header("select_slider")
initilise_slider_variable = st.select_slider("choose a level",options = options_level)
st.write("you just chose : ",initilise_slider_variable)


st.title("slider -2")

#here we will start workign with the range to selct the data

options_level_range = range(0,100)

initilise_slider_variable_from_range = st.select_slider("choose a level",options = options_level_range)
st.write("you just chose : ",initilise_slider_variable_from_range)
st.write("you chose %s hearts"%initilise_slider_variable_from_range,initilise_slider_variable_from_range*":hearts:")
st.write("you chose %s fire"%initilise_slider_variable_from_range,initilise_slider_variable_from_range*":fire:")


st.header("slider")


#you can choose to have a min and max variables
st.title("Slider-3")
initilise_slider_variable_from_range_min_max = st.slider("choose a level : ",min_value=0.0, max_value=1.0, step=0.1)
st.write("you just chose : ",initilise_slider_variable_from_range_min_max)


st.title("Streamlit slider")
st.subheader("Slider for best")
x = st.slider("A number between 0-100",value = 50)
st.write("you choose : ",x) 


st.title("new value applied in the slider variable the slider wuld be just stay stagnate at 100")
x_100 = st.slider("A number between 0-100",value = 100)
st.write("you choose for the function varialbe 100 : ",x_100)



st.title("Radio Button")
range_value  = ["option-1","option-2","option-3"]
page_radio = st.radio("Click on",range_value)
st.write("you choose",page_radio)

st.header("if else applied")

st.title("Radio Button range_value_if_else")
range_value_if_else  = ["option-a","option-b","option-c"]
page_radio_if_else = st.radio("Click on",range_value_if_else)
st.write("you choose",page_radio_if_else)

if page_radio_if_else == "option-1":
  st.write("welcome to 1")
else:
  st.write("you choose",page_radio_if_else)
