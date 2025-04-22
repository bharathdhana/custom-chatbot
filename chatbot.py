from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I am a chatbot."]],
    ["how are you?", ["I'm doing great, thanks!"]],
    ["quit", ["Bye-bye!"]],
]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
