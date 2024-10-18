import streamlit as st


#read in css
with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

pages = [
    #Pages tbd
    st.Page('app/src/home.py',title='MTA Base', icon=':material/domain:', default=True),
    st.Page('app/src/log.py',title='MTA Log', icon=':material/map:'),
    st.Page('app/src/mta_analysis.py',title='MTA Ridership', icon=':material/groups:'),
    st.Page('app/src/mta_suggestions.py',title='MTA Line Suggestion', icon=':material/subway:'),
    st.Page('app/src/mta_ai.py',title='MT-AI', icon=':material/robot_2:'),
    st.Page('app/src/my.py',title='CREDITS', icon=':material/contact_page:')
]

#set streamlit navigation to follow pages list
pg = st.navigation(pages)
pg.run()