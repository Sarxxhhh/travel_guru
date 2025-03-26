import streamlit as st
from openai import OpenAI
import openai

# openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Travel Guru", page_icon="🌍")
st.title("🌍 Travel Guru: Your Personalized Itinerary Planner")

destination = st.text_input("Where are you going?")
duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30, step=1)
start_location = st.text_input("Where are you traveling from?")
preferences = st.text_area("Your Interests (e.g. food, culture, adventure)")
budget = st.selectbox("Budget Level", ["Budget", "Mid-range", "Luxury"])
dates = st.text_input("Travel Dates (optional)")

if st.button("Generate Itinerary"):
    with st.spinner("Planning your perfect trip..."):
        user_prompt = f"""
        Create a {duration}-day travel itinerary from {start_location} to {destination}.
        Preferences: {preferences}. Budget: {budget}.
        Travel dates: {dates if dates else 'not specified'}.
        Structure the itinerary by day, include morning/afternoon/evening activities, minimize travel time, and suggest places to eat or explore.
        """
      
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful travel planner named Travel Guru."},
        {"role": "user", "content": user_prompt}
    ]
)
st.markdown(response["choices"][0]["message"]["content"])
