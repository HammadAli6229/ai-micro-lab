#!/usr/bin/env python
# coding: utf-8

# # CHATBOT WITH RULE-BASED RESPONSES
# 
# Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow.

# In[1]:


import re

def simple_chatbot(user_input):
    # Convert user input to lowercase to make it case-insensitive
    user_input = user_input.lower()
    
    # Define some predefined patterns and responses using regular expressions
    patterns = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you|how r u': 'I am just a computer program, but thanks for asking!',
        r'what is your name': 'I am a simple chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day!'
    }
    
    # Check if the user input matches any of the predefined patterns
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    
    # If no match is found, return a default response
    return "I'm sorry, I don't understand that."

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = simple_chatbot(user_input)
    print(f"Chatbot: {response}")


# In[ ]:




