import streamlit as st

animes = [
    "Attack on Titan", "My Hero Academia", "Demon Slayer", "One Piece", "Naruto",
    "Death Note", "Fullmetal Alchemist: Brotherhood", "Jujutsu Kaisen",
    "Tokyo Revengers", "Spy x Family", "Dragon Ball Z", "Bleach", "One Punch Man",
    "Hunter x Hunter", "Sword Art Online", "Black Clover", "Fairy Tail", "Re:Zero",
    "Steins;Gate", "Code Geass", "Neon Genesis Evangelion", "Cowboy Bebop",
    "Akame ga Kill!", "Blue Exorcist", "Parasyte: The Maxim", "Your Lie in April",
    "Vivy: Fluorite Eye's Song", "The Seven Deadly Sins", "Noragami", "Erased",
    "JoJo's Bizarre Adventure", "KonoSuba", "The Rising of the Shield Hero",
    "Made in Abyss", "Mushoku Tensei: Jobless Reincarnation",
    "The Ancient Magus' Bride", "The Devil is a Part-Timer!", "No Game No Life",
    "Akudama Drive", "Baccano!", "Durarara!!", "Gintama", "Hellsing Ultimate",
    "Paranoia Agent", "Samurai Champloo", "Terror in Resonance",
    "The Garden of Sinners", "The Melancholy of Haruhi Suzumiya",
    "The World God Only Knows", "Toradora!", "Your Name.", "Weathering with You",
]

mejor_anime = "JoJo's Bizarre Adventure"

st.title("Lista de los mejores animes de la historia")

for anime in animes:
    st.write(f"- {anime}")

respuesta = st.text_input("¿Cuál es el mejor anime de la historia?")

if st.button("Comprobar"):
    if respuesta.strip().lower() == mejor_anime.lower():
        st.success(f"¡Correcto! {mejor_anime} es el mejor anime de la historia.")
    else:
        st.error(f"Incorrecto. La respuesta correcta es {mejor_anime}.")
        st.write(f"Mírate {mejor_anime}, ya de ya es obligatorio.")
