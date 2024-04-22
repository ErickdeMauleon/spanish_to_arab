import pandas as pd
import streamlit as st

# Lista de letras del teclado
teclado = [
    ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ'][::-1],
    ['د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص'][::-1],
    ['ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق'][::-1],
    ['ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'][::-1],
    ['ء', 'آ', 'أ', 'ٱ', 'إ', 'ئ', 'ى'][::-1],
    ['ة', 'ؤ', 'َ', 'ً', 'ُ', 'ٌ', 'ّ'][::-1],
    ['ْ', 'ِ', 'ٍ', 'ٰ', 'ٖ', 'ٗ', 'space'][::-1]
]

# Crear el contenedor con st.markdown
def contenedor_html(word, color_fondo):
    return f"""
    <div style="background-color: {color_fondo}; padding: 10px; border-radius: 5px;font-size: 30px">
        <div style="text-align: right">{word}</div>
    </div>
"""

# Cuadro de texto para mostrar la entrada del teclado
if "entrada_teclado" not in st.session_state:
    st.session_state.entrada_teclado = ""

# if "arab_words" not in st.session_state:
#     st.session_state.arab_words = pd.read_csv('Data/Arab words.csv')
#     st.session_state.arab_words.columns = ['Spanish', 'Pronunciation', 'Arabic']

if "vocabulary" not in st.session_state:
    st.session_state["vocabulary"] = (pd.read_csv('Data/arab vocabulary.csv'
                                                 , usecols="Español	Ingles	Arabe	Pronunciacion	Categoria".split("\t")
                                                )
                                      .query('Categoria.notnull()')
                                    )
    st.session_state["vocabulary"]["weight_to_sample"] = 1
    st.session_state["category"] = list(st.session_state["vocabulary"]["Categoria"].unique())
    st.session_state["category"].sort()


# Crear la interfaz del teclado
st.title('Translate from spanish to arabic')



category = st.selectbox('Select a category', st.session_state["category"])

if "random_word" not in st.session_state:
    st.session_state.random_word = st.session_state["vocabulary"].query('Categoria == @category').sample(n=1)

if st.button('New word', key='new'):
    st.session_state.random_word = st.session_state["vocabulary"].query('Categoria == @category').sample(n=1, weights='weight_to_sample')
    st.session_state.entrada_teclado = ""



# st.write('Translate from spanish to arabic: '+st.session_state.random_word['Spanish'].values[0])
st.write('Translate from spanish to arabic: '+st.session_state.random_word['Español'].values[0] + ' (%s)' % st.session_state.random_word['Ingles'].values[0])

tab1, tab2 = st.tabs(['Online keyboard', 'I have a keyboard'])

tries = 0

with tab1:
    a1, a2, a3, a4, a5, a6, a7 = st.columns(7)
    b1, b2, b3, b4, b5, b6, b7 = st.columns(7)
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    d1, d2, d3, d4, d5, d6, d7 = st.columns(7)
    e1, e2, e3, e4, e5, e6, e7 = st.columns(7)
    f1, f2, f3, f4, f5, f6, f7 = st.columns(7)
    g1, g2, g3, g4, g5, g6, g7 = st.columns(7)

    for i, col in enumerate([a1, a2, a3, a4, a5, a6, a7]):
        if col.button(teclado[0][i], key=teclado[0][i]):
            st.session_state.entrada_teclado += teclado[0][i]

    for i, col in enumerate([b1, b2, b3, b4, b5, b6, b7]):
        if col.button(teclado[1][i], key=teclado[1][i]):
            st.session_state.entrada_teclado += teclado[1][i]

    for i, col in enumerate([c1, c2, c3, c4, c5, c6, c7]):
        if col.button(teclado[2][i], key=teclado[2][i]):
            st.session_state.entrada_teclado += teclado[2][i]

    for i, col in enumerate([d1, d2, d3, d4, d5, d6, d7]):
        if col.button(teclado[3][i], key=teclado[3][i]):
            st.session_state.entrada_teclado += teclado[3][i]

    for i, col in enumerate([e1, e2, e3, e4, e5, e6, e7]):
        if col.button(teclado[4][i], key=teclado[4][i]):
            st.session_state.entrada_teclado += teclado[4][i]

    for i, col in enumerate([f1, f2, f3, f4, f5, f6, f7]):
        if col.button(teclado[5][i], key=teclado[5][i]):
            st.session_state.entrada_teclado += teclado[5][i]

    for i, col in enumerate([g1, g2, g3, g4, g5, g6, g7]):
        if col.button(teclado[6][i], key=teclado[6][i]):
            if teclado[6][i] == 'space':
                st.session_state.entrada_teclado += ' '
            else:
                st.session_state.entrada_teclado += teclado[6][i] 

    z1, z2, z3, z4, z5, z6, z7 = st.columns(7)
    # Botón para borrar la entrada del teclado
    if z1.button('Clean all', key='clean'):
        st.session_state.entrada_teclado = ""

    if z2.button('Delete', key='delete'):
        st.session_state.entrada_teclado = st.session_state.entrada_teclado[:-1]

    if z3.button('Show', key='show'):
        st.write(st.session_state.random_word['Arabe'].values[0] + ' (%s)' % st.session_state.random_word['Pronunciacion'].values[0])
        tries += 0.5

    st.markdown(contenedor_html(st.session_state.entrada_teclado, "#DCE7FA"), unsafe_allow_html=True)



with tab2:

    st.session_state.entrada_teclado = st.text_area('Enter the text in arabic:', value=st.session_state.entrada_teclado, height=5)

    _z1, _, _, _, _, _, _ = st.columns(7)

    if _z1.button('Show', key='show2'):
        st.write(st.session_state.random_word['Arabe'].values[0] + ' (%s)' % st.session_state.random_word['Pronunciacion'].values[0])
        tries += 0.5




def check_word(word):
    if st.session_state.random_word['Arabe'].values[0] == word:
        return True
    else:
        return False
    
if st.button('Check', key='check'):
    if check_word(st.session_state.entrada_teclado):
        # Markdown Correct in green
        st.markdown('<p style="color:Green;">Correct</p>', unsafe_allow_html=True)
        st.session_state.entrada_teclado = ""
        st.session_state["vocabulary"].loc[st.session_state.random_word.index, 'weight_to_sample'] += tries
    else:
        # Markdown Incorrect in red
        st.markdown('<p style="color:Red;">Incorrect</p>', unsafe_allow_html=True)
        tries += 1



