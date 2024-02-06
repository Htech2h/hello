import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load pre-trained GPT-2 model and tokenizerssssssssss
model_name = 'gpt2-medium'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the device for inference
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

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
pdf_directory = 'CalcI_Complete.pdf'
pdf_texts = []
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        pdf_text = load_and_preprocess_pdf(pdf_path)
        preprocessed_text = preprocess_text(pdf_text)
        pdf_texts.append(preprocessed_text)

# Tokenize and fine-tune the model on the preprocessed PDF texts
tokenized_texts = [tokenizer.encode(text, return_tensors='pt') for text in pdf_texts]
input_ids = torch.cat(tokenized_texts, dim=0).to(device)

# Fine-tune the model on the tokenized text data (not implemented here)

# Generate text based on a given prompt
def generate_text(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    with torch.no_grad():
        output = model.generate(input_ids, max_length=150, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Generate text using the trained model
input_prompt = "solve the inverse of y =2x+2"
generated_text = generate_text(input_prompt)
print("Generated Text:")
print(generated_text)
