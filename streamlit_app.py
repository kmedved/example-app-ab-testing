import streamlit as st
import pandas as pd

def update_elo_ratings(rating1, rating2, result, k_factor=32):
    prob1 = 1 / (1 + 10**((rating2 - rating1) / 400))
    prob2 = 1 / (1 + 10**((rating1 - rating2) / 400))

    new_rating1 = rating1 + k_factor * (result - prob1)
    new_rating2 = rating2 + k_factor * ((1 - result) - prob2)
    
    return new_rating1, new_rating2

def main():
    st.title("NBA Players Elo Comparison")

    # Replace this with your own NBA players data
    data = {
        'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'James Harden', 'Russell Westbrook'],
        'Elo': [2500, 2400, 2300, 2200, 2100]
    }

    df = pd.DataFrame(data)
    
    player1 = st.selectbox('Select Player 1:', df['Player'])
    player2 = st.selectbox('Select Player 2:', df['Player'][df['Player'] != player1])

    p1_elo, p2_elo = df[df['Player'] == player1]['Elo'].values[0], df[df['Player'] == player2]['Elo'].values[0]

    if st.button('Compare Players'):
        result = 1 if p1_elo > p2_elo else 0
        new_p1_elo, new_p2_elo = update_elo_ratings(p1_elo, p2_elo, result)

        st.write(f"**{player1}** Elo: {p1_elo:.0f} -> {new_p1_elo:.0f}")
        st.write(f"**{player2}** Elo: {p2_elo:.0f} -> {new_p2_elo:.0f}")
    
        winner = player1 if result == 1 else player2
        st.write(f"**{winner}** is the better player according to the Elo ratings.")

if __name__ == "__main__":
    main()