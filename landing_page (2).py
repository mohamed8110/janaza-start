import streamlit as st

st.set_page_config(page_title="Janaza Documenten", layout="centered")
st.title("📄 Janaza Documentenportaal")

st.markdown("Welkom bij het centrale Janaza-portaal. Kies hieronder het document dat u wilt genereren:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧾 Attest Rituele Verzorging")
    st.link_button("➡️ Open", "https://janaza-attest.streamlit.app/")

with col2:
    st.markdown("### 🖊️ Mandaat")
    st.link_button("➡️ Open", "https://janaza-mandaat.streamlit.app/")

with col3:
    st.markdown("### ❤️ Liefdadigheidsverklaring")
    st.link_button("➡️ Open", "https://janaza-liefdadigheid.streamlit.app/")