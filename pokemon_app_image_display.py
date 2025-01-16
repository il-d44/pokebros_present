import streamlit as st


# Title for the app
st.title("Pokémon Image Viewer")

# Input for Pokémon number
pokemon_number = st.text_input("Enter Pokémon Number between 1 and 898:")

# Validate user input
if pokemon_number.isdigit() and 1 <= int(pokemon_number) <= 898:
    # Format the Pokémon number with leading zeros
    formatted_number = pokemon_number.zfill(3)
    
    # Construct the image URL
    image_url = f"https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/{formatted_number}.png"
    
    # Display the image
    st.image(image_url, caption=f"Pokémon #{formatted_number}")
else:
    st.warning("Please enter a valid number between 1 and 898.")

