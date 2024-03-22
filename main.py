import telebot
import requests
import currency_converter

bot = telebot.TeleBot('your token')
c = currency_converter.CurrencyConverter

@bot.message_handler(['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Погоду в каком городе вы хотите узнать?')

@bot.message_handler()
def word(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=87d64de4dbe70550e4219b98bee2109b'
    weather = requests.get(url).json()
    temperature = round(weather['main']['temp'])
    feels_like = round(weather['main']['feels_like'])
    osadki = round(weather['wind']['speed'])
    description = weather["weather"][0]["description"]
    gradus1 = 'градуса'
    if temperature > 4:
        gradus1 = 'градусов'
    elif temperature == 1 :
        gradus1 = 'градус'
    bot.reply_to(message, f'Погода в {city} - {description},сейчас {temperature} {gradus1}, ощущается как {feels_like} {gradus1}, скорость ветра - {osadki} м/с ')

bot.polling(none_stop=True)
