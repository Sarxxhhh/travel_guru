import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="Travel Guru", page_icon="🌍")
st.title("🌍 Travel Guru: Your Personalized Itinerary Planner")

# User inputs
destination = st.text_input("Where are you going?")
duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30, step=1)
start_location = st.text_input("Where are you traveling from?")
preferences = st.text_area("Your Interests (e.g. food, culture, adventure)")
budget = st.selectbox("Budget Level", ["Budget", "Mid-range", "Luxury"])
dates = st.text_input("Travel Dates (optional)")

# When user clicks the button
if st.button("Generate Itinerary"):
    with st.spinner("Planning your perfect trip..."):

        # Prompt with clear instructions and time-stamp format
        prompt = f"""
        You are a travel planning assistant. Create a detailed {duration}-day travel itinerary from {start_location} to {destination}.

        User preferences: {preferences}. Budget: {budget}. Travel dates: {dates if dates else 'not specified'}.

        For **each day**, structure the plan like this:
        - **Morning** (include specific time-stamped activities, e.g., "8:00 AM – Breakfast at X")
        - **Afternoon** (e.g., "1:30 PM – Visit local museum")
        - **Evening** (e.g., "7:00 PM – Dinner at rooftop restaurant")

        🕒 Important: Every activity must include a specific time (e.g., "3:30 PM – Relax at XYZ Café").

        Keep travel minimal, match the user's interests, and include unique spots (local restaurants, cultural sights, hidden gems).
        """

        # OpenAI API call using new SDK
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful travel planner named Travel Guru."},
                {"role": "user", "content": prompt}
            ]
        )

        # Show the result
        st.markdown(response.choices[0].message.content)
