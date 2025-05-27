# AI--Powered-Task-Management-System
An intelligent Task Management System that integrates Sentiment Analysis, Task Optimization, and Forecasting to streamline project and task handling. This AI-powered tool is designed to assist teams and project managers in making data-driven decisions by understanding emotional context, forecasting productivity, and optimizing workload distribution

# About the Project
This project showcases the power of combining machine learning models with project management workflows. The system comprises three core components:
Sentiment Analysis: Utilizes a Multinomial Naive Bayes classifier trained on Twitter data to classify task descriptions as positive or negative, helping teams understand emotional nuances behind assigned work.
Task Optimization: Implements a Random Forest Regressor to estimate the number of hours required for tasks based on features like priority, deadline, and estimated workload, enhancing resource allocation and planning.
Task Forecasting: Uses the ARIMA model for the time series forecasting to predict the number of task completions in the coming week, offering insights into team productivity trends and helping plan future workloads.

# Tools & Technologies Used
Data Science & Machine Learning
Python Libraries: NumPy, Pandas, Scikit-learn, NLTK, Statsmodels
Models:
Naive Bayes Classifier - For sentiment classification
Random Forest Regressor - For workload prediction
ARIMA - For time-series task forecasting

Preprocessing:
Regular expressions
Stopword removal
TF-IDF vectorization

Web Frameworks & Deployment
Streamlit - For building an interactive and real-time UI
Flask -To deploy ML Models as APIS
Joblib/Pickle - For model serialization and loading

# Insights & Outcomes
Better Task Planning: Predicts task duration based on context, improving time and resource management.
Emotional Context in Workflows: Understands the tone behind task descriptions, suporting empathetic and efficient prioritization.
Productivity Forecasting: Estimates how many tasks will be completed in the near future, helping in goal tracking and trend analysis.
