import streamlit as st 
import pandas as pd
import numpy

st.markdown("# Pokebros Present POKEDEX3000")
st.subheader("Choose your Pokemon")

# DATA FORMATTING AND MANAGEMENT
try:
    pokedex_db = pd.read_csv('pokemon.csv')
except FileNotFoundError:
    st.error("The file 'pokemon.csv' was not found. Please ensure it is in the same directory.")
pokedex_db.rename(columns={pokedex_db.columns[0]: 'Duplicate Identifier'}, inplace=True)








pokedex_id = st.number_input("Please enter Pokemon Number ", min_value=1, max_value=898)


if pokedex_id in pokedex_db['pokedex_number'].values:
    pokemon = pokedex_db[pokedex_db['pokedex_number'] == pokedex_id]
    if len(pokemon) > 1:
        pokemon_chooser = st.empty()
        pokemon_chooser.dataframe(pokemon)
        select_box = st.selectbox('There are a few pokemon with the same pokedex number, choose which pokemon with the Duplicate Identifier', pokemon['name'])
        pokemon_chooser.empty()
        st.dataframe(pokedex_db[pokedex_db.iloc[:, 0] == select_box])
    else:
        st.dataframe(pokemon)
else:
    st.warning("No Pokémon found with that number.")
