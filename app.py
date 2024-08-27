import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

# st.write
st.header('st.write')

# sample 1
st.write('Hello: *World!* :sunglasses:')

# sample 2
st.write(1234)

# sample 3
df= pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

st.write(df)

# sample 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe')

# sample 5
df2= pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b','c']
)
st.write(df2)
c=alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c']
)

st.write(c)

# st.slider
import streamlit as st
from datetime import time, datetime

st.header('st.slider')
# sample 1
st.subheader('Slider')

age=st.slider("How old are you?", 0, 130, 25)
st.write("I'm", age, "years old")

# sample 2
st.subheader('Range slider')
values=st.slider("Select a range of values",0.0,100.0,(25.0, 75.0))
st.write("Value:",values)

# sample 3
st.subheader('Range time slider')
appointment=st.slider("Schedule your appointment:", 
                      value=(time(11,30),time(12,45)))
st.write("you're scheduled:", appointment)

# sample 4
st.subheader('Datetime slider')
start_time=st.slider('When do you start',
                     value=datetime(2020,1,1,9,30),
                     format="MM/DD/YY - hh:mm")
st.write("Start time:",start_time)

# st.line_chart
st.header('Line chart')
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.write(chart_data)
st.line_chart(chart_data)

#st.altair_chart
# import altair as alt
# from vega_datasets import data

# source=data.cars()

# chart=alt.Chart(source).mark_circle().encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color='Origin'
# ).interactive()
# tab1,tab2=st.tabs(["Streamlit theme (default)", "Altair native theme"])

# with tab1:
#     st.altair_chart(chart, theme='streamlit', use_container_width=True)
# with tab2:
#     st.altair_chart(chart,theme=None, use_container_width=True)

#st.selectbox
st.header('st.selectbox')

option=st.selectbox(
    "What's your favorite color?",
    ('Blue','Green','Red'))

st.write('Your favorite color is ',option)

#st.multiselect
st.header('st.multiselect')

options=st.multiselect(
    "What are your favorite colors?",
    ['Blue', 'Green', 'Red', 'Yellow'],
    ['Yellow', 'Red'])

st.write("Your favorite colors are ", options)

#st.checkbox
st.header("st.checkbox")
st.write("What do you want to order?")
icecream=st.checkbox("Ice cream")
coffee=st.checkbox("Coffee")
cola=st.checkbox("Cola")

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")