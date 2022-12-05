import altair as alt
import pandas as pd
import streamlit as st
import cohere 
import prompttextclexit as ptc
import prompttextsnaturalnews as ptnn
import prompttextbowl as ptb
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

# initialize the Cohere Client with an API Key
co = cohere.Client('Ni4Rck1QBU4ODHfUpb2pKWOSgLm7Y6qYTUHeVQtz') 

# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------- FUNCTIONS ---------------------------------------------------------------------

text = ptc.text1
summary = ptc.summary1

text2 = ptb.text3
summary2 = ptb.summary3

def inform_me(input):
    if len(input) == 0:
        return None
    if ''+textOrUrl+'' == 'Text':
        response = co.generate( 
        model='large', 
        prompt=f'[{text}:{summary}\
        --\
        {text2}:{summary2}\
        --\
        {input}:', 
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
        prompt=f' {input}',
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
    page_title="DiscernAI", page_icon="🧠", layout="wide"
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
* **Python libraries:**  streamlit, requests, json, time
* **Data source:**
* **Credit:** Web scraper adapted from).
""")

st.markdown(
    """
    Example misinformation text:
"""
)
st.markdown(
    """

    "In recent years the government has been pushing \"energy providers\" to install smart meters in every home in the UK. As we have come to learn, anything that is pushed by the government usually has an agenda behind it so why are they so desperate to get these meters in our homes?\
On the 1st October the government announced that it would be collecting, storing and processing all British smart meter data. This is despite assurances given over many years that the data was under the control of households and only they could access it. It could not be shared without their express permission and it could only be used for billing purposes.\
We also have to ask can they control how much energy we use? If they decide we are using too much or want to control usage at peak times, can they simply switch off our supply remotely? Their motives certainly appear sinister and there needs to be push back as this is just another step towards digital slavery.\
You do not have to agree to having a smart meter fitted, it is your right to refuse it despite what your \"energy provider\" may tell you. They are under pressure from the government and will do their best to coerce you into having one. If you already have smart meters fitted you can request to have them removed.\
Your data is your most precious thing. Ditch your smart meters if you have them. They are just another control mechanism. Just say no."
"""
)
st.markdown(
    """
    Example factual text text:
"""
)
st.markdown(
    """
    "bowling, also called tenpins, game in which a heavy ball is rolled down a long, narrow lane toward a group of objects known as pins, the aim being to knock down more pins than an opponent. The game is quite different from the sport of bowls, or lawn bowls, in which the aim is to bring the ball to rest near a stationary ball called a jack.\
    There are many forms of bowling, but tenpins, the most widely played variation, is the principal form in the United States, Canada, western Europe, East Asia, Australia, New Zealand, and Latin America. Its many variations include duckpins, candlepins, fivepins, skittles, and ninepins, with differences within the framework of each of the games."
"""
)

if ''+textOrUrl+'' == 'Text':
    input = st.text_area('Enter your text', height=100)
else:
    input = st.text_area('Enter your webiste URL', height=100)
st.button('Inform me', on_click = inform_me(input))
if "inform_me" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.inform_me = st.write("waiting for input")
else:
    st.write(st.session_state.output)