import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm a chatbot, so I don't have feelings, but I'm here to help!"],
    "what's your name": ["I'm just a chatbot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
}

def response_generator(user_input):
    user_input=user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return "I'm sorry, I don't understand what your query is!!.Please rephrase your question?"

print("ChatBot: Hi! I'm ChatBot. How can I assist you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break
    response = response_generator(user_input)
    print("ChatBot:", response)