import streamlit as st
from datetime import datetime

st.subheader('1. Text Input')
name = st.text_input('Enter your name : ', value = 'Satyam Kumar Jha')
st.write('Hello', name)

st.subheader('2. Password Input')
password = st.text_input('Enter your password : ',type = 'password', help = 'Atleast have 8 characters')

st.subheader('3. Text Area')
st.text_input('Tell me something about yourself in 200 words', max_chars = 300, help = 'Maximum 300 characters are allowed' )

st.subheader('4. Numeric Input')
st.number_input('Enter your age : ',min_value = 0,max_value = 110, step = 1, value = 24)

st.subheader('5. Date Input')
today = datetime.now().date()
date = st.date_input('Enter the date : ', value = today, min_value = today, max_value = today.replace(year = today.year + 1))
st.write("You've selected : ",datetime.strftime(date,'%m/%d/%y'))

st.subheader('6. Radio Button')
gender = st.radio('Sele ct your gender : ',options = ('Male','Female','other'),help = 'Choose One', horizontal = True)
st.write("You've selected",gender)

st.subheader('7. Select Box')
option = st.selectbox('Select your options : ',options = ('Data Analysis','ML','DL','AI','other'),help = 'Choose One')
st.write("You've selected",option)

st.subheader('8. Multi-Select Box')
options = st.multiselect('Select the options : ', options = ('Data Analysis','ML','DL','AI'),help = 'You can select multi options')

st.subheader('9. Botton')
if st.button('Say Hello'):
    st.write('Hi')

st.subheader('10. Checkbox')
if st.checkbox('I agree to the terms and conditions.', help = 'You must agree to proceed '):
    st.write('Thanks you for agreeing')

st.subheader('11. Color Picker')
color = st.color_picker('Select your favourite color :')
st.write("You've selected",color,'color')    

st.button('Submit your Response')
