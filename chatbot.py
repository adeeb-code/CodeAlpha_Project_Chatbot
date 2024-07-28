import nltk
from nltk.chat.util import Chat, reflections
import requests
import datetime
import json

# Download necessary NLTK data
nltk.download('punkt')
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        weather_description = weather['description']
        return f"The temperature in {city} is {temperature - 273.15:.2f}°C with {weather_description}."
    else:
        return "Sorry, I couldn't retrieve the weather information right now."

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def perform_arithmetic(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return "I can only perform basic arithmetic operations like add, subtract, multiply, and divide."
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How are you doing today?", "Hi %1! Nice to meet you. How's your day going?",]
    ],
    [
        r"hi|hey|hello",
        [f"{get_greeting()} How can I assist you today?", "Hey there! What's up?", "Hi! How's it going?",]
    ],
    [
        r"what is your name ?",
        ["I'm a friendly chatbot created by you. You can call me ChatBot. What's your name?",]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great! How about you?", "I'm here to help you. How are you feeling today?",]
    ],
    [
        r"sorry (.*)",
        ["No worries at all!", "It's all good!", "Don't worry about it!",]
    ],
    [
        r"I am (.*) good|fine|okay|alright",
        ["That's great to hear!", "Awesome! How can I assist you today?", "Glad to hear that. What's on your mind?",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help! What do you need assistance with?", "Of course! What do you need help with?",]
    ],
    [
        r"quit",
        ["Goodbye! Take care!", "It was nice chatting with you. See you soon!", "Bye! Have a great day!"]
    ],
    [
        r"(.*) weather in (.*)",
        [(lambda matches: get_weather(matches[1])),]
    ],
    [
        r"(.*) (created|made) (.*)",
        ["I was created by a clever developer using Python. Do you like programming?",]
    ],
    [
        r"(.*) (favorite|like) (.*)",
        ["I don't have preferences, but I think everything is interesting in its own way!", "I can't say I have a favorite, but I'm here to learn from you!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"(.*) (add|subtract|multiply|divide) (.*) and (.*)",
        [(lambda matches: f"The result is {perform_arithmetic(matches[1], float(matches[2]), float(matches[3]))}"),]
    ],
]
def chatbot():
    print("Hi! I am your friendly chatbot. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()