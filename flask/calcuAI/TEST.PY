
import torch
#from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer




# Function to load and preprocess text data from PDFs
def load_and_preprocess_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_text = ""
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        return pdf_text

# Function for text preprocessing
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

# Load and preprocess multiple PDFs
pdf_directory = "CalcI_Complete.pdf"
pdf_texts = []
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        pdf_text = load_and_preprocess_pdf(pdf_path)
        preprocessed_text = preprocess_text(pdf_text)
        pdf_texts.append(preprocessed_text)

print(pdf_text)