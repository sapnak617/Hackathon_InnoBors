import re
import time

import nltk
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()


# Escape Markdown metacharacters so user-supplied text is rendered verbatim
# rather than interpreted (prevents markdown injection: links, images that
# trigger outbound requests, headers, etc.).
_MARKDOWN_SPECIALS = re.compile(r'([\\`*_{}\[\]()#+\-.!>|~])')


def escape_markdown(text: str) -> str:
    return _MARKDOWN_SPECIALS.sub(r'\\\1', text)

# Set up the Streamlit app
st.title("Sentiment Analysis Chatbot")
st.write("Enter a sentence and I'll classify it as positive, negative, or neutral!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history. User-authored content was escaped on the way in,
# so rendering with st.markdown here is safe.
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
    # Escape user-supplied text before storing/rendering to prevent markdown
    # injection (links, remote images, layout spoofing). The raw `prompt` is
    # still passed to the analyzer unchanged so sentiment scoring is unaffected.
    safe_prompt = escape_markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": safe_prompt})

    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(safe_prompt)

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
