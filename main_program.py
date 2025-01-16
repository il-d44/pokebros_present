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

pokedex_id = st.number_input("Please enter Pokemon Number ", min_value=1, max_value=99999)

with st.expander("Secret Pokemon"):
    st.write("Enter 99999 for a look at an unreleased secret pokemon")

if pokedex_id in pokedex_db['pokedex_number'].values:
    pokemon = pokedex_db[pokedex_db['pokedex_number'] == pokedex_id]
    if len(pokemon) > 1:
        pokemon_chooser = st.empty()
        pokemon_chooser.dataframe(pokemon)
        select_box = st.selectbox('There are a few pokemon with the same pokedex number, choose which pokemon with the Duplicate Identifier', pokemon['name'])
        pokemon_chooser.empty()
        st.dataframe(pokedex_db[pokedex_db.iloc[:, 2] == select_box])
    else:
        st.dataframe(pokemon)
else:
    st.warning("No Pokémon data.")



# IMAGE DISPLAY


# Title for the app
st.title("Pokémon Image Viewer")

# Input for Pokémon number
str_pokedex_id = str(pokedex_id)

# Validate user input
if str_pokedex_id.isdigit() and 1 <= int(str_pokedex_id) <= 898:
    # Format the Pokémon number with leading zeros
    formatted_number = str_pokedex_id.zfill(3)
    
    # Construct the image URL
    image_url = f"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{formatted_number}.png"
    
    # Display the image
    st.image(image_url, caption=f"Pokémon #{formatted_number}")
if pokedex_id == 99999:
    st.image('ryanchu.jpg', caption='Ryanchu', width=400)
else:
    st.warning("Please enter a valid number between 1 and 898.")


# GRAPHING

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
    st.session_state.random_pokemon = pick_random(pokedex_db)

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


