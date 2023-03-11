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

# Define our Streamlit app
def run_app():
    st.title("NBA Player Comparison")

    # Ask the user to compare players
    player1, rating1 = random.choice(list(players.items()))
    player2, rating2 = random.choice(list(players.items()))
    st.write(f"Compare {player1} vs {player2}:")
    choice = st.radio("", (player1, player2))
    if choice == player1:
        score1, score2 = 1, 0
    else:
        score1, score2 = 0, 1

    # Update the Elo ratings and display the current rankings
    players[player1], players[player2] = update_ratings(rating1, rating2, score1, score2)
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    st.write("Current Rankings:")
    for i, (player, rating) in enumerate(sorted_players):
        st.write(f"{i+1}. {player} ({rating:.0f})")

# Run the app
run_app()