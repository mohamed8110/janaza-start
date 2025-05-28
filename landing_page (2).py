import streamlit as st

st.set_page_config(page_title="Janaza Documentenportaal", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #2c3e50;'>📄 Janaza Documentenportaal</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Welkom bij het centrale portaal voor het genereren van documenten bij Janaza VZW.</p>",
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3376/3376949.png", width=80)
    st.markdown("### 🧾 Attest Rituele Verzorging")
    st.link_button("➡️ Open", "https://janaza-attest.streamlit.app/")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=80)
    st.markdown("### 🖊️ Mandaat")
    st.link_button("➡️ Open", "https://janaza-mandaat.streamlit.app/")

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/4202/4202843.png", width=80)
    st.markdown("### ❤️ Liefdadigheidsverklaring")
    st.link_button("➡️ Open", "https://janaza-liefdadigheid.streamlit.app/")
