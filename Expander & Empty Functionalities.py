import time
import numpy as np
import pandas as pd
import streamlit as st

# Simulate 100 dice rolls
cases = [np.random.randint(1, 7) for _ in range(100)]

# Count occurrences for each face (1 to 6)
data = [cases.count(i) for i in range(1, 7)]

# Create a DataFrame with labels
df = pd.DataFrame({
    'Face': [1, 2, 3, 4, 5, 6],
    'Frequency': data
})

st.header('🎲 Frequency of Dice Faces (1 to 6)')
st.bar_chart(df.set_index('Face'))  # Set 'Face' as index

with st.expander('See Explanation'):
    st.write('''
        The chart shows some numbers I got from rolling a dice 100 times and its
        basically about how many times each face appears
        ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")


with st.empty():
    st.write('You need to wait for 10 seconds')
    for seconds in range(11):
        st.write('⏳ ' + str(seconds) + ' seconds remained')
        time.sleep(1)
    st.write('10 seconds completed')
