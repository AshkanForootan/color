import streamlit as st

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for color in colors:
    st.write('<span style="color:%s">%s</span>' % (color, color), unsafe_allow_html=True)