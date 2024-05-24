import telebot
import requests
import json
from telebot import types

TOKEN = '####' #API Bot
API_ENDPOINT = 'http://x.x.x.x:1234/v1/chat/completions' #IP Server


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "AI BOT Chat")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_input = message.text

    api_data = {
        "messages": [
            {"role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 50,
        "stream": False
    }

    response = requests.post(API_ENDPOINT, json=api_data, headers={"Content-Type": "application/json"})


    if response.status_code == 200:
        api_response = json.loads(response.text)

        assistant_response = api_response["choices"][0]["message"]["content"]

        bot.reply_to(message, assistant_response)
    else:
        bot.reply_to(message, "Error")


if __name__ == "__main__":
    bot.polling(none_stop=True)
