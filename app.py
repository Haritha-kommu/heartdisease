import streamlit as st
import joblib

clf=joblib.load('hdp.joblib')

st.title("HEART DISEASE PREDICTION")
a=st.number_input('Enter  age')
c=st.number_input('Enter  no.of cigs per day ')
tc=st.number_input('Enter  total cholestrol')
sbp=st.number_input('Enter sysBP ')
dbp=st.number_input('Enter  disBP')
bmi=st.number_input('Enter BMI ')
hr=st.number_input('Enter heart rate ')
g=st.number_input('Enter gloucose ')

if st.button('PREDICT'):
    prediction=clf.predict([[a,c,tc,sbp,dbp,bmi,hr,g]])
    if prediction==0:
        st.text('NO chance for CHD')
    else:
        st.text('YES chance for CHD')
