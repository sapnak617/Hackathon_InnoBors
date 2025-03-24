# Sentiment Analysis Chatbot

This is a simple sentiment analysis chatbot that classifies sentences as positive, negative, or neutral using NLTK's VADER sentiment analyzer.

## Requirements

- Python 3.7+
- Streamlit
- NLTK

## Installation

1. First, install the required packages:

```bash
pip install streamlit nltk
```

2. Save the provided Python code as `sentiment_chatbot.py`

## Running the App

To run the application, open your terminal/command prompt, navigate to the directory containing the saved Python file, and run:

```bash
streamlit run sentiment_chatbot.py
```

This will start a local Streamlit server and automatically open the app in your default web browser (usually at http://localhost:8501).

## How to Use

1. Type any sentence in the input box at the bottom of the page
2. Press Enter to submit your text
3. The chatbot will analyze the sentiment and display the result, including:
   - Overall sentiment classification (Positive, Negative, or Neutral)
   - Detailed breakdown of sentiment scores

## How It Works

The application uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer, which is specifically tuned for social media text but works well for most casual text. VADER uses a lexicon of words rated for sentiment, along with rules for things like punctuation, capitalization, and modifiers.

The sentiment classification is based on the compound score:
- Positive: compound score >= 0.05
- Negative: compound score <= -0.05
- Neutral: compound score between -0.05 and 0.05

The breakdown scores show the proportion of text that falls in each category (positive, negative, neutral) and the normalized compound score.
