import streamlit as st
import numpy as np
import pandas as pd
import time
chart_data = pd.DataFrame(
        np.random.randn(30, 3),
        columns=['a', 'b', 'c'])
option = st.sidebar.selectbox(
    "which number do you like best?",
    chart_data['a']
)
'You  selected:', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me')
if pressed:
    right_column.write('wohoo')
expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really lond explanations.....")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)