#import the streamlit library
import streamlit as st

#give the app a name
st.title("Welcome to Adanna's BMI Calculator")
st.text("Body mass index (BMI) is a measure of body fat based on height and weight \nthat applies to adult men and women.")

# Import picture

from PIL import Image
image = Image.open("bodymassindex.JPG")

st.image(image, width = 500)

# Take the weight in Kilograms
weight = st.number_input("Enter your weight (in kgs)")

#Take Height Input
#radio button to choose height format
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if (status == 'cms'):
        height = st.number_input('Centimeters')
        try:
                bmi = weight / ((height/100) ** 2)
        except:
                st.text("Enter some value of height")
elif (status == 'meters'):
        height = st.number_input('Meters')
        try:
                bmi : weights/(height ** 2)
        except:
                st.text("Enter some value of height")

        # 1 meter = 3.28
if (status == 'feet'):
        height = st.number_input('feet')
        try:
                bmi = weight / (((height/3.28)) ** 2)
        except:
                st.text("Enter some value of height")

if (st.button('Calculate BMI')):
      #
        st.text("Your BMI Index is {}. ".format(bmi))

              # give the interpretation of BMI index

        if (bmi < 16):

                st.error("You are Extremely Underweight")

        elif (bmi >= 16 and bmi < 18.5):

                st.warning("You are Underweight")

        elif (bmi >= 18.5 and bmi < 25):

                st.success("Healthy")

        elif (bmi >= 25 and bmi < 30):

                st.warning("Overweight")

        elif (bmi >= 30):

                st.error("Extremely Overweight")

st.text('For more information click the link below')
st.link_button("Podcast E39", "https://www.youtube.com/watch?v=l1BMPoonf9U")
