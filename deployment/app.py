import streamlit as st
from sentida import Sentida
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Dansk Sentiment Scoring",
    page_icon="🇩🇰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar with table of contents
with st.sidebar:
    st.header("Indholdsfortegnelse")
    section = st.radio("Gå til sektion:", ["Om appen", "Analysér enkelt tekst", "Analysér og sammenlign to tekster", "Analysér og plot længere tekst"])
 

# App title
st.title('💡Dansk sentiment scoring💡')

# Section 1: About the App
if section == "Om appen":
    st.header("Om appen")
    st.markdown("""
        - Denne app udfører sentimentanalyse på dansk tekst.
        - Scorerne varierer fra -1 (negativt) til 1 (positivt).
        - Du kan analysere en enkelt tekst, sammenligne to tekster eller plotte sentiment for længere tekster.
        - ⬅️ Vælg den service du ønsker i menuen til venstre. ⬅️

    """)

# Section 2: Single text analysis
if section == "Analysér enkelt tekst":
    # Header
    st.header('🔍 Analysér enkelt tekst')

    # Information about sentiment scoring
    st.markdown("""
        Tilføj din tekst og få udregnet den gennemsnitlige sentiment score for den samlede tekst.
    """)

    # Text input from user
    user_input = st.text_area("Skriv din tekst her:")

    # Button to analyze the sentiment
    if st.button("Analysér tekst"):
        if user_input:
            # Calculate sentiment score
            sentiment_score = Sentida().sentida(user_input, output="mean")
            # Display the sentiment score
            st.write(f"Sentiment score: {sentiment_score}")
        else:
            st.write("Please enter some text for analysis.")
        

# Section 3: Two texts comparison
if section == "Analysér og sammenlign to tekster":
    # Header
    st.header('📊 Analysér og sammenlign to tekster')

    # Information about sentiment scoring
    st.markdown("""
        Tilføj to forskellige tekster og få visualiseret sammenligningen.
    """)

    # Text input for comparison
    tekst_1 = st.text_area("Tilføj første tekst:")
    tekst_2 = st.text_area("Tilføj anden tekst:")

    # Comparison button
    if st.button("Sammenlign resultater"):
        sentiment_1 = Sentida().sentida(tekst_1, output="mean")
        sentiment_2 = Sentida().sentida(tekst_2, output="mean")
        st.write(f"Sentiment score af tekst 1: {sentiment_1}")
        st.write(f"Sentiment score af tekst 2: {sentiment_2}")
        # Display a bar chart for comparison
        st.bar_chart({"Tekst 1": sentiment_1, "Tekst 2": sentiment_2})
        

# Section 4: Sentiment plot for longer text
if section == "Analysér og plot længere tekst":
    # Header
    st.header('📈 Analysér og plot længere tekst')

    # Information about sentiment scoring
    st.markdown("""
        - Tilføj en længere tekst bestående af flere sætninger.
        - Den gennemsnitlige sentiment score af hver enkelt sætning udregnes og plottes.
    """)

    # Text input from user
    user_input_2 = st.text_area("Skriv din tekst her")

    # Ploting button
    if st.button("Analysér og plot tekst"):
        if user_input_2:
            # Split text into sentences and 
            sentences = user_input_2.split('.')
            # Remove any empty list objects 
            sentences = [sentence for sentence in sentences if sentence]
            # Get sentiment scores for each sentence
            sentence_scores = [Sentida().sentida(sentence, output="mean") for sentence in sentences]
            
            # Dynamically adjust plot width based on the number of sentences
            width = min(15, max(6, len(sentences) // 3))  # Set minimum and maximum width for the figure
            
            # Plot the sentiment scores
            plt.figure(figsize=(width, 4))  # Dynamically adjust the plot width based on the number of sentences
            plt.plot(sentence_scores, marker='o')
            # Use the sentences as x-tick labels 
            plt.xticks(range(len(sentences)), sentences, rotation=45, ha="right")  # Rotate labels for better readability
            plt.title("Sentiment Score Over Time")
            plt.xlabel("Sentence")
            plt.ylabel("Sentiment Score")
            st.pyplot(plt)