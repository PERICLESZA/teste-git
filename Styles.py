import streamlit as st

def overlay_area(label, conteudo):
    input_id = st.empty()
    st.markdown(
        f'<label for="{input_id.empty().id}" style="position: absolute; font-size: 13px; top: -65px; left: 0px; background-color: #586E75; border-radius: 5px;padding: 0 5px;">{label}</label>',
        unsafe_allow_html=True,
    )
    return input_id.empty().text_area("", conteudo, key={label}, label_visibility='collapsed')

    # Customer.attention = st.text_area("Obs:", Customer.attention)

def overlaid_input(label, conteudo):
    input_id = st.empty()
    st.markdown(
        f'<label for="{input_id.empty().id}" style="position: absolute; font-size: 13px; top: -65px; left: 0px; background-color: #586E75; border-radius: 5px;padding: 0 5px;">{label}</label>',
        unsafe_allow_html=True,
    )
    return input_id.empty().text_input("", conteudo, key={label}, label_visibility='collapsed')

def overlaid_date(label, conteudo):
    input_id = st.empty()
    st.markdown(
        f'<label for="{input_id.empty().id}" style="position: absolute; font-size: 13px; top: -65px; left: 0px; background-color: #586E75; border-radius: 5px; padding: 0 5px;">{label}</label>',
        
        unsafe_allow_html=True,
    )
    return input_id.empty().date_input("", conteudo, key=None, label_visibility='collapsed')

def overlaid_number(label, formt):
    input_id = st.empty()
    input_key = f"{label}_number_input"  # Gere uma chave única com base no rótulo
    st.markdown(
        f'<label for="{input_id.empty().id}" style="position: absolute; font-size: 13px; top: -65px; left: 0px; background-color: #586E75; border-radius: 5px;padding: 0 5px;">{label}</label>',
        unsafe_allow_html=True,
    )
    return input_id.empty().number_input('', format=formt, key=input_key, label_visibility='collapsed')

def overlaid_selectbox(label, options, index, form_f):
    selectbox_id = st.empty()
    st.markdown(
        f"""
        <label for="{selectbox_id.empty().id}" style="position: absolute; font-size: 13px; top: -65px; left: 0px; background-color: #586E75; border-radius: 5px;padding: 0 5px;">{label}</label>
        <style>
            #{selectbox_id.empty().id} select {{margin-top: 10px;}}
        </style>
        """,
        unsafe_allow_html=True,
    )
    return selectbox_id.empty().selectbox("", options,  index, form_f, label_visibility='collapsed')

def overlaid_area(label, conteudo):
    input_id = st.empty()
    st.markdown(
        f'<label for="{input_id.empty().id}" style="position: absolute; font-size: 13px; top: -148px; left: 0px; background-color: #586E75; border-radius: 5px;padding: 0 5px;">{label}</label>',
        unsafe_allow_html=True,
    )
    return input_id.empty().text_area("", conteudo, key={label}, label_visibility='collapsed')


