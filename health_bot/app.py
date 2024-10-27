import streamlit as st
from transformers import pipeline

# Load the model for text generation
model_name = "google/flan-t5-small"  # You can adjust this model if needed
nlp = pipeline("text2text-generation", model=model_name, clean_up_tokenization_spaces=True)

# Streamlit app layout
st.title("Health Symptom Checker Chatbot")
st.write("Describe your symptoms to receive possible explanations.")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to get response from the model
def get_response(symptoms):
    input_text = f"What could be the reason for symptoms like {symptoms}?"
    response = nlp(input_text, max_new_tokens=50)[0]['generated_text']
    return response

# User input
user_input = st.text_input("Enter your symptoms:")

# Respond when user enters symptoms
if user_input:
    # Get response from the model
    response = get_response(user_input)
    
    # Append user input and bot response to chat history
    st.session_state.chat_history.append(("User", user_input))
    st.session_state.chat_history.append(("Bot", response))

    # Clear user input
    user_input = ""

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Bot:** {message}")
