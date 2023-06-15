import requests
from bs4 import BeautifulSoup
import telebot
import time

# Задаем параметры для подключения к Telegram API
bot_token = '6070063901:AAHNEpIQgF0FTZQUP6XZeOR5_EKjyKO2GEo'
chat_id = '5551202557'

# Создаем объект бота
bot = telebot.TeleBot('6070063901:AAHNEpIQgF0FTZQUP6XZeOR5_EKjyKO2GEo')

# Задаем URL сайта, который будем отслеживать
urlpage = 'https://mosk.minsk.gov.by/zhilishchnaya-politika/arendnoe-zhiljo/zhilye-pomeshcheniya-kommercheskogo-ispolzovaniya'

# Получаем HTML-код страницы
response = requests.get(urlpage)
soup = BeautifulSoup(response.content, 'html.parser')

# Извлекаем текст из HTML-кода страницы
page_text = soup.get_text()

# Запоминаем текущий текст страницы
previous_page_text = page_text

while True:
    # Получаем новый HTML-код страницы
    response = requests.get(urlpage)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлекаем новый текст из HTML-кода страницы
    page_text = soup.get_text()

    # Сравниваем новый текст с предыдущим
    if page_text != previous_page_text:
        # Если текст изменился, отправляем уведомление в Telegram
        message = f'Сайт {urlpage} был изменен'
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json)
       # bot.send_message(chat_id=chat_id, text=message)
        previous_page_text = page_text

    # Ждем 10 секунд перед повторным запросом
    time.sleep(60)
