import collections
import streamlit as st
from pages import utils


def app():
    st.markdown("## Page 1")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.")
    st.write("\n")
