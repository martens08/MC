import streamlit as st
message = 'COSES QUE VULL FER AMB TU ABANS DE MARXAR:\n\n- Excursió a la muntanya\n- Un viatge curt de dos dies :)\n- Jugar a padel\n- Anar a escalar\n- Fer qualsevol esport tb\n- No fer res\n- Dormir junts jeje\n- Anar a un concert junts\n- Sortir de festa (pero no gaire)\n- Mirar fotos de petits\n- Parlar de coses no importants (alguna important tb)\n- Riure molt\n- Moltes abraçades, petons i +\n- I qualsevol cosa que tu vulguiss'
st.title("JOC REGAL")

st.info("Introdueix la contrasenya per desbloquejar un missatge secret")


input = st.text_input("Contrasenya: ", value=" ")

if input == '2ANYSMC':
    with st.expander('MISSATGE DESBLOQUEJAT'):
        st.write(message)
elif input != ' ':
    st.write('Contrasenya Erronia')