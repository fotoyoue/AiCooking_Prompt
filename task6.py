import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
from nltk import FreqDist
import string

# Function to extract keywords using a simplified RAKE approach
def extract_keywords(text, top_n=5):
    # Tokenize the text
    words = word_tokenize(text, engine='newmm')
    
    # Remove stopwords, punctuation, and empty strings
    stopwords = list(thai_stopwords())
    words = [word for word in words if word not in stopwords and word not in string.punctuation and word.strip()]
    
    # Calculate word frequencies
    freq_dist = FreqDist(words)
    
    # Get the top_n keywords
    keywords = [word for word, freq in freq_dist.most_common(top_n)]
    
    return '|'.join(keywords)

# Read the input CSV file
test_df = pd.read_csv('test.csv')

# Process each text in the test dataframe
test_df['keywords'] = test_df['text'].apply(lambda x: extract_keywords(x, top_n=5))

# Select only the id and keywords columns for output
output_df = test_df[['id', 'keywords']]

# Save the output to a CSV file
output_df.to_csv('out.csv', index=False)
