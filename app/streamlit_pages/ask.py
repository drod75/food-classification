import streamlit as st

#read in css
with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' 
                , unsafe_allow_html=True)

st.header('Food Classify: Ask')
st.write('')

with st.container(border=True):
    st.write('Hello')
