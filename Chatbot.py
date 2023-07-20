import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

successful_interactions = 0
user_needs = ["get information", "ask a question", "request assistance"]

chatbot_personality = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "positive": ["Great", "Awesome", "Fantastic"],
    "negative": ["I'm sorry.", "Apologies.", "My apologies."],
    "unknown": ["I'm not sure.", "I don't know.", "I can't answer that."]
}

chatbot_flow = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you today?"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "positive": ["I'm glad you're satisfied!", "I'm happy to help!", "You're welcome!"],
    "negative": ["I'm sorry to hear that.", "I'll do my best to improve.", "I apologize for any inconvenience."],
    "unknown": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure how to respond."],
    "Info": [
        "A friendly chatbot is a conversational AI program that is designed to interact with users in a pleasant and helpful manner. It is programmed to understand and respond to user queries, provide information, and assist with tasks in a friendly and approachable way.",
        "Ask any question you want."
    ]
}

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    return " ".join(tokens)

def get_user_input():
    user_input = input("You: ")
    return preprocess_input(user_input)

def generate_chatbot_response(user_input):
    chatbot_response = ""
    user_input = user_input.lower()

    if any(need in user_input for need in user_needs):
        chatbot_response = random.choice(chatbot_flow["Info"])
        global successful_interactions
        successful_interactions += 1
    elif any(greeting in user_input for greeting in ["hi", "hello"]):
        chatbot_response = random.choice(chatbot_flow["greeting"])
    elif any(positive in user_input for positive in ["great", "awesome"]):
        chatbot_response = random.choice(chatbot_flow["positive"])
    elif any(goodbye in user_input for goodbye in ["bye", "goodbye"]):
        chatbot_response = random.choice(chatbot_flow["farewell"])
    else:
        chatbot_response = random.choice(chatbot_flow["unknown"])
    return chatbot_response

def start_chatbot():
    print("Welcome to Chatbot!")
    print("Chatbot:", "How may I assist you today?")
    
    while True:
        user_input = get_user_input()
        if user_input == "exit":
            break
        chatbot_response = generate_chatbot_response(user_input)
        print("Chatbot:", chatbot_response)

    print("Successful Interactions:", successful_interactions)

start_chatbot()
