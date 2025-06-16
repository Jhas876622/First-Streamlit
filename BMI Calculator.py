import streamlit as st

def rate_yourself():
    with st. sidebar:
        st.title('Rate Yourself')
        languages = st.text_input(
            'Enter the programming languages you know (comma-separated):',
            value='Python'
        )
        languages = [lang.strip() for lang in languages.split(',')]

    st.subheader('How would you rate your experience in the following programming languages/tools?')
    for language in languages:
        st.write(f'🛠 {language}')
        st.slider(f'Rate your skill in {language}', min_value=0.0, max_value=10.0, step=0.5)


def BMI_calculator():
    st.title("💪 BMI Calculator")

    with st.form(key='BMI Calculator', clear_on_submit=False):
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            weight = st.number_input("Enter your weight (in kg)", min_value=0.0)
        with col2:
            height = st.number_input("Enter your height (in meters)", min_value=0.0)
        with col3:
            submit = st.form_submit_button(label='Calculate')

    if submit:
        if height == 0:
            st.warning("⚠️ Height cannot be zero. Please enter a valid value.")
        else:
            bmi = round((weight / height**2), 2)
            st.write(f"📏 Your BMI is: **{bmi}**")

            if bmi <= 18.5:
                st.error("You are Underweight 🦴")
            elif bmi <= 24.9:
                st.success("You have a Healthy / Normal BMI 🥦")
            elif bmi <= 29.9:
                st.warning("You are Overweight 🍕")
            else:
                st.error("You are Obese 🚨")


# Sidebar menu
st.sidebar.title("📋 Select an Option")
choice = st.sidebar.selectbox('Menu', ['BMI', 'Rate Yourself'])

# Load selected function
if choice == 'BMI':
    BMI_calculator()
elif choice == 'Rate Yourself':
    rate_yourself()
