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

# git test