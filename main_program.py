import streamlit as st 
import pandas as pd
import numpy
import altair as alt

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
    if len(pokemon) > 1:
        st.image(image_url, caption=f"Pokémon #{formatted_number} Name: {select_box}")
    else:
        st.image(image_url, caption=f"Pokémon #{formatted_number}")
if pokedex_id == 99999:
    st.image('ryanchu.jpg', caption='Ryanchu', width=400)
elif pokedex_id < 1 or pokedex_id > 898 or pokedex_id != 99999:
    st.warning("Please enter a valid number between 1 and 898.")


# GRAPHING

#Filtering columns from selected pokemon
pokemon = pokedex_db[pokedex_db['pokedex_number'] == pokedex_id]
pokemon_stats = pokemon[['name', 'height_m', 'weight_kg']]

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
    all_pokemon = pd.concat([random_pokemon, pokemon_stats])
    st.dataframe(all_pokemon)

    # Add spacing between the charts
    st.write("\n")  # Adds vertical space

    # Plot height 
    pkmn_height_chart = (
        alt.Chart(all_pokemon)
        .mark_bar(size=35)
        .encode(
            x=alt.X("name:N", sort=None, title=None),
            y=alt.Y("height_m:Q", title="Height (m)"),
            color=alt.Color("name:N", legend=None),
        )
        .properties(
            title="Height of Pokémon",
            width=500,  # Adjust the width
            height=550,  # Adjust the height
        )
        .configure_title(
            fontSize=20,  # Set the title font size
            fontWeight="bold",  # Optionally make it bold
            anchor="start",  # Align the title to the left
            color="white",  # Optionally set the title color
        )
    )
    st.altair_chart(pkmn_height_chart)

    # Plot weight 
    pkmn_weight_chart = (
        alt.Chart(all_pokemon)
        .mark_bar(size=35)
        .encode(
            x=alt.X("name:N", sort=None, title=None),
            y=alt.Y("weight_kg:Q", title="Weight (kg)"),
            color=alt.Color("name:N", legend=None),
        )
        .properties(
            title="Weight of Pokémon",
            width=500,  # Adjust the width
            height=550,  # Adjust the height
        )
        .configure_title(
            fontSize=20,  # Set the title font size
            fontWeight="bold",  # Optionally make it bold
            anchor="start",  # Align the title to the left
            color="white",  # Optionally set the title color
        )
    )
    st.altair_chart(pkmn_weight_chart)


