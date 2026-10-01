import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("FitBuddy - AI Fitness Plan Generator 💪")
st.write("Your personal AI fitness assistant powered by Gemini")

genai.configure(api_key="test")
model = genai.GenerativeModel('gemini-1.5-flash')

age = st.number_input("Enter your Age", min_value=10, max_value=80, value=22)
weight = st.number_input("Enter Weight (kg)", min_value=30, max_value=150, value=60)
height = st.number_input("Enter Height (cm)", min_value=100, max_value=220, value=165)
goal = st.selectbox("Select your Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])

def generate_fitness_plan(age, weight, height, goal, diet):
    prompt = f"Create fitness plan for Age {age}, Weight {weight}kg, Height {height}cm, Goal {goal}, Diet {diet}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return f"Workout Plan for {goal}, Diet Plan for {diet}, 2000 calories, Age {age} Weight {weight}kg"

if st.button("Generate My Fitness Plan"):
    plan = generate_fitness_plan(age, weight, height, goal, diet)
    st.success(plan)
