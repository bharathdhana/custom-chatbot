from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I am a chatbot."]],
    ["how are you?", ["I'm doing great, thanks!"]],
    ["what is your favorite color?", ["I like all colors!"]],
    ["what is your favorite food?", ["I don't eat, but I love pizza!"]],
    ["tell me a joke", ["Why did the chicken cross the road? To get to the other side!"]],
    ["what is the weather like?", ["I don't know, but I hope it's nice!"]],
    ["what is your favorite movie?", ["I love all movies!"]],
    ["what is your favorite book?", ["I love all books!"]],
    ["what is your favorite music?", ["I love all music!"]],
    ["what is your favorite sport?", ["I love all sports!"]],
    ["what is your favorite hobby?", ["I love all hobbies!"]],
    ["what is your favorite animal?", ["I love all animals!"]],
    ["what is your favorite place?", ["I love all places!"]],
    ["what is your favorite season?", ["I love all seasons!"]],
    ["what is your favorite holiday?", ["I love all holidays!"]],
    ["what is your favorite time of day?", ["I love all times of day!"]],
    ["what is your favorite thing to do?", ["I love all things!"]],
    ["what is your favorite quote?", ["I love all quotes!"]],
    ["what is your favorite saying?", ["I love all sayings!"]],
    ["what is your favorite word?", ["I love all words!"]],
    ["quit", ["Bye-bye!"]],
]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
