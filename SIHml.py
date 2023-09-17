class ArohanMitra:
    def __init__(self):
        self.responses = {
            "en": {
                "greeting": "Hello! How can I help you?",
                "farewell": "Goodbye! Have a great day!",
            },
            "hi": {
                "greeting": "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
                "farewell": "फिर मिलें! आपका दिन शुभ हो!",
            },
            "or": {
                "greeting": "ନମସ୍କାର! ମୋ କିପରିମାଣ କରିପାରୁ?",
                "farewell": "ପୁଣି ମିଳ୍ଲି ଆମ୍ବକ! ଆପଣଙ୍କ ଦିନ ସୁଖମ୍!",
            }
        }

    def set_language(self, language):
        self.language = language

    def get_response(self, key):
        if self.language in self.responses:
            if key in self.responses[self.language]:
                return self.responses[self.language][key]
        return "Sorry, I don't understand that."



ArohanMitra = ArohanMitra()

print("Select a language:")
print("1. English (en)")
print("2. Hindi (hi)")
print("3. Odia (or)")

language_choice = input("Enter the language code (en/hi/or): ")

ArohanMitra.set_language(language_choice)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = ArohanMitra.get_response(user_input)
    print("ArohanMitra:", response)
