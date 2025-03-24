import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

# Download VADER lexicon if not already downloaded
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Set up the Streamlit app
st.title("Sentiment Analysis Chatbot")
st.write("Enter a sentence and I'll classify it as positive, negative, or neutral!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to analyze sentiment - simplified to return only the category
def analyze_sentiment(text):
    # Get sentiment scores
    scores = sia.polarity_scores(text)
    
    # Determine sentiment category
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# User input
prompt = st.chat_input("Type a sentence here...")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display bot thinking indicator
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Analyzing sentiment...")
        
        # Analyze sentiment - now just returns the category
        sentiment = analyze_sentiment(prompt)
        
        # Create simplified response - just the category
        full_response = f"{sentiment}"
        
        # Simulate typing
        time.sleep(0.5)
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})