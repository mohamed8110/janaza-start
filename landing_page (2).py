import streamlit as st

st.set_page_config(page_title="Janaza Documentenportaal", layout="wide")

# Header met logo en titel
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("logo.png", width=80)
with col_title:
    st.markdown(
        "<h1 style='color: #2c3e50;'>📄 Janaza Documentenportaal</h1>",
        unsafe_allow_html=True
    )

st.markdown("<p style='text-align: left;'>Welkom bij het centrale portaal voor het genereren van documenten bij Janaza VZW.</p>", unsafe_allow_html=True)
st.markdown("---")

# Stijl voor knopkaarten
st.markdown("""
<style>
.card-button {
    display: block;
    padding: 20px;
    text-align: center;
    background-color: #f1f1f1;
    border-radius: 10px;
    border: 1px solid #ddd;
    text-decoration: none;
    color: black;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.2s ease-in-out;
}
.card-button:hover {
    background-color: #e6e6e6;
    border-color: #aaa;
}
</style>
""", unsafe_allow_html=True)

# Knoppen als kaarten
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3376/3376949.png", width=60)
    st.markdown("<a href='https://janaza-attest.streamlit.app/' class='card-button'>🧾 Attest</a>", unsafe_allow_html=True)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=60)
    st.markdown("<a href='https://janaza-mandaat.streamlit.app/' class='card-button'>🖊️ Mandaat</a>", unsafe_allow_html=True)

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/4202/4202843.png", width=60)
    st.markdown("<a href='https://janaza-liefdadigheid.streamlit.app/' class='card-button'>❤️ Liefdadigheid</a>", unsafe_allow_html=True)
