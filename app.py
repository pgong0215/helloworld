import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

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