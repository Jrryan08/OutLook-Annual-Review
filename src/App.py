import streamlit as st
from PIL import Image
import codecs
import streamlit.components.v1 as components

#page navigations
Welcome = st.Page("Welcome.py", title="Welcome", icon="🌝")
About = st.Page("About.py", title="About", icon="🌝")
Explore = st.Page("Explore.py", title="Explore", icon="📈")
Visualizations = st.Page("Visualizations.py", title="Visualizations", icon="🌝")
Predictions = st.Page("Predictions.py", title="Predictions", icon="🌝")
Conlusion = st.Page("Conlusion.py", title="Conlusion", icon="🎬")

page = st.navigation([Welcome,About,Explore,Conlusion,Visualizations,Predictions ])
page.run()