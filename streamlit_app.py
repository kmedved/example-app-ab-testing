import streamlit as st
import pandas as pd
import random

def update_elo_ratings(rating1, rating2, result, k_factor=32):
    prob1 = 1 / (1 + 10**((rating2 - rating1) / 400))
    prob2 = 1 / (1 + 10**((rating1 - rating2) / 400))

    new_rating1 = rating1 + k_factor * (result - prob1)
    new_rating2 = rating2 + k_factor * ((1 - result) - prob2)
    
    return new_rating1, new_rating2

def select_new_players(df):
    player1, player2 = random.sample(df['Player'].tolist(), 2)
    return player1, player2

def main():
    st.title("NBA Players Elo Comparison")

    # Replace this with your own NBA players data
    data = {
        'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'James Harden', 'Russell Westbrook'],
        'Elo': [2500, 2400, 2300, 2200, 2100]
    }

    df = pd.DataFrame(data)

    session_state = st.session_state

    if "player1" not in session_state or "player2" not in session_state:
        session_state.player1, session_state.player2 = select_new_players(df)

    st.write(f"**Player 1:** {session_state.player1}")
    st.write(f"**Player 2:** {session_state.player2}")

    choice = st.radio("Who is the better player?", (session_state.player1, session_state.player2))

    if st.button('Submit'):
        result = 1 if choice == session_state.player1 else 0
        p1_elo, p2_elo = df[df['Player'] == session_state.player1]['Elo'].values[0], df[df['Player'] == session_state.player2]['Elo'].values[0]
        new_p1_elo, new_p2_elo = update_elo_ratings(p1_elo, p2_elo, result)

        st.write(f"**{session_state.player1}** Elo: {p1_elo:.0f} -> {new_p1_elo:.0f}")
        st.write(f"**{session_state.player2}** Elo: {p2_elo:.0f} -> {new_p2_elo:.0f}")
    
        winner = session_state.player1 if result == 1 else session_state.player2
        st.write(f"**{winner}** is the better player according to the Elo ratings.")
        
        session_state.player1, session_state.player2 = select_new_players(df)

if __name__ == "__main__":
    main()