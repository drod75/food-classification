import streamlit as st


#read in css
with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' 
                , unsafe_allow_html=True)

#Pages
pages = [
    st.Page('app/streamlit_pages/ask.py',title='Food Classify', icon=':material/search:', default=True),
    st.Page('app/streamlit_pages/metrics.py',title='Food CNN Metrics', icon=':material/dashboard:')
]

#set streamlit navigation to follow pages list
pg = st.navigation(pages)
pg.run()