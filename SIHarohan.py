from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a ChatBot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot and train it on the English language
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # You can train it on other languages too

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        response = chatbot.get_response(user_message)
        return jsonify({'response': str(response)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
