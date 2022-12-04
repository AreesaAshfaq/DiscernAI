import altair as alt
import pandas as pd
import streamlit as st
from vega_datasets import data


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

alt.themes.enable("streamlit")

st.set_page_config(
    page_title="DiscernAI", page_icon="⬇", layout="wide"
)

# Generate a sidebar for the streamlit app

# st.sidebar.image(
#     "",
#     width=200,
#     use_column_width=False,
#     output_format="PNG",
#     caption="DiscernAI",
# )

st.sidebar.text("v1.0.0")

st.sidebar.title("DiscernAI")
st.sidebar.markdown(
    """
    This is a web application for the DiscernAI project. The purpose of this app is to
    allow users to quickly analyse whether the contents of a webpage are misinformation
    and create a short summary of its contents.
    """
)

# -------------------------------------------------------------------------------------------------------------------




# ----------------------------------  MAIN PAGE ---------------------------------------------------------------------
st.title("DiscernAI")
st.write("v1.0.0 by Discern")

st.header("👋 Introduction")
st.markdown(
    """
    If you're interested in world stability and the biases in the information available to you,
    well who isn't? We're here to help you discriminate between misinformation and unbiased sources.
    \n
    #### This application will help you:
    - 👀 Quickly analyse the biases in a webpage or article
    - 💬 Summarise the contents of that page
    - 🔦 Shine a light on the way the information is being framed to shape your opinion
"""
)
