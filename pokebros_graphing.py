import streamlit as st
import pandas as pd
import altair as alt

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

    # Add spacing between the charts
    st.write("\n")  # Adds vertical space

    # Create two columns for graphs with padding
    height_col, weight_col = st.columns([1, 1], gap="large")

    # Plot height in one column
    with height_col:
        pkmn_height_chart = (
            alt.Chart(random_pokemon)
            .mark_bar(size=35)
            .encode(
                x=alt.X("name:N", sort=None, title=None),
                y=alt.Y("height_m:Q", title="Height (m)"),
                color=alt.Color("name:N", legend=None),
            )
            .properties(
                title="Height of Pokémon",
                width=400,  # Adjust the width
                height=450,  # Adjust the height
            )
            .configure_title(
                fontSize=20,  # Set the title font size
                fontWeight="bold",  # Optionally make it bold
                anchor="start",  # Align the title to the left
                color="white",  # Optionally set the title color
            )
        )
        st.altair_chart(pkmn_height_chart)

    # Plot weight in another column
    with weight_col:
        pkmn_weight_chart = (
            alt.Chart(random_pokemon)
            .mark_bar(size=35)
            .encode(
                x=alt.X("name:N", sort=None, title=None),
                y=alt.Y("weight_kg:Q", title="Weight (kg)"),
                color=alt.Color("name:N", legend=None),
            )
            .properties(
                title="Weight of Pokémon",
                width=400,  # Adjust the width
                height=450,  # Adjust the height
            )
            .configure_title(
                fontSize=20,  # Set the title font size
                fontWeight="bold",  # Optionally make it bold
                anchor="start",  # Align the title to the left
                color="white",  # Optionally set the title color
            )
        )
        st.altair_chart(pkmn_weight_chart)
