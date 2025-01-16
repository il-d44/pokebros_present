import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('pokemon.csv')

# Select 5 random Pokémon
def pick_random(df):
    random_pokemon = df.sample(5)[['name', 'height_m', 'weight_kg']]
    return random_pokemon

# Initialize session state for the button
if "show_data" not in st.session_state:
    st.session_state.show_data = False

# Layout for the page
st.subheader("5 Random Pokémon")

# Button to show data
if st.button("Show 5 Random Pokémon"):
    st.session_state.show_data = True
    st.session_state.random_pokemon = pick_random(data)

# Conditionally display the data frame and graphs
if st.session_state.show_data:
    # Display the DataFrame
    random_pokemon = st.session_state.random_pokemon
    st.dataframe(random_pokemon)

    # Create two columns for graphs
    height_col, weight_col = st.columns(2)

    # Plot height in one column
    with height_col:
        pkmn_height_info = random_pokemon.set_index('name')[['height_m']]
        st.bar_chart(pkmn_height_info)

    # Plot weight in another column
    with weight_col:
        pkmn_weight_info = random_pokemon.set_index('name')[['weight_kg']]
        st.bar_chart(pkmn_weight_info)
