import streamlit as st
import requests

st.title("AI Powered Task Management System")

text_input = st.text_area("Enter task description for sentiment analysis.")


if st.button('Analyze Sentiment'):
    response = requests.post('http://localhost:5001/predict_sentiment', json={'text': text_input})
     
    if response.status_code == 200:
        sentiment = response.json().get('sentiment', 'No sentiment returned')
        st.write(f'The task sentiment is: {sentiment}')
    else:
        st.write("Error in sentiment analysis")


priority = st.selectbox("Select Task Priority", ['low', 'medium', 'high'])


deadline = st.number_input("Enter Deadline (in days)", min_value=1, max_value=30)
workload = st.number_input("Enter Estimated Workload (in hours)", min_value=1, max_value=24)

if st.button('Optimize Task'):
    priority_mapping = {'low': 1, 'medium': 2, 'high': 3}
    priority_numeric = priority_mapping.get(priority, 1)

    response = requests.post('http://localhost:5001/optimize_task', json={'priority_numeric': priority_numeric, 'deadline': deadline, 'workload': workload})


    if response.status_code == 200:
        predicted_workload = response.json().get('predicted_workload', 'No prediction returned')
        st.write(f'Predicted hours for task completion: {predicted_workload}')

    else:
        st.write("Error in task optimization")