import altair as alt
import pandas as pd
import streamlit as st
import cohere 

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

# initialize the Cohere Client with an API Key
co = cohere.Client('Ni4Rck1QBU4ODHfUpb2pKWOSgLm7Y6qYTUHeVQtz')

# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------- FUNCTIONS ---------------------------------------------------------------------



def inform_me(input):
    if len(input) == 0:
        return None
    if ''+textOrUrl+'' == 'Text':
        response = co.generate( 
        model='large', 
        prompt='summarise this text and tell me if there\'s any misinformation.'.format(input), 
        max_tokens=100, 
        temperature=0.1, 
        k=0, 
        p=1, 
        frequency_penalty=0, 
        presence_penalty=0, 
        stop_sequences=["--"], 
        return_likelihoods='NONE') 
        
        st.session_state['output'] = response.generations[0].text
        st.balloons()
    else:
        ## Scrape URL and put text to input
        input = input
        ### Continue
        response = co.generate( 
        model='large', 
        prompt='summarise this text and tell me if there\'s any misinformation.'.format(input), 
        max_tokens=100, 
        temperature=0.1, 
        k=0, 
        p=1, 
        frequency_penalty=0, 
        presence_penalty=0, 
        stop_sequences=["--"], 
        return_likelihoods='NONE') 
        
        st.session_state['output'] = response.generations[0].text
        st.balloons()


alt.themes.enable("streamlit")
# -------------------------------------------------------------------------------------------------------------------




# -------------------------------------- SIDEBAR ---------------------------------------------------------------------
# Generate a sidebar for the streamlit app
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
textOrUrl= st.sidebar.selectbox('Are you entering a Text or URL', ('Text', 'URL'))
# -------------------------------------------------------------------------------------------------------------------




# ----------------------------------  MAIN PAGE ---------------------------------------------------------------------
#---------------------------------#
# Title
st.title("DiscernAI")
st.write("v1.0.0 by Discern")

#---------------------------------#
# introduction
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
#---------------------------------#
# about
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:**
* **Credit:** Web scraper adapted from).
""")
if ''+textOrUrl+'' == 'Text':
    input = st.text_area('Enter your text', height=100)
else:
    input = st.text_area('Enter your webiste URL', height=100)
st.button('Inform me', on_click = inform_me(input))