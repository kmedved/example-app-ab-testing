import numpy as np
import streamlit as st
import random

# Define our initial player data
players = {
    "LeBron James": 1000,
    "Kobe Bryant": 1000,
    "Michael Jordan": 1000,
    "Shaquille O'Neal": 1000,
    "Magic Johnson": 1000
}

# Initialize the Elo rating system
K = 32  # The K factor determines how much ratings change after each game
def expected_score(rating1, rating2):
    return 1 / (1 + 10 ** ((rating2 - rating1) / 400))
def update_ratings(rating1, rating2, score1, score2):
    expected1 = expected_score(rating1, rating2)
    expected2 = expected_score(rating2, rating1)
    rating1 += K * (score1 - expected1)
    rating2 += K * (score2 - expected2)
    return rating1, rating2

def run_app():
    st.title("Fruit Selection")

    option = st.selectbox("Select a fruit", ["Apple", "Orange"])

    if option:
        st.write(f"You selected {option}")

# Run the app
run_app()