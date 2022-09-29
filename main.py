from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

chrome_options =Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)
nav.get("https://casino.betfair.com/pt-br/c/roleta")

time.sleep(5)
token = '5619862462:AAEkDj4ksz5rgMP4CaK_IHArYlqFSl688JA'
chat_id = '-837954839'
estrategia5 = "19,28"


def estrategias():
    pass



def telegram_mensage(token, chat_id, mensagem):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}'
    return requests.get(url)

while True:

    lista = []

    for x in range(1):

        elem = nav.find_elements(By.CLASS_NAME, 'number')

        elem2 = elem[x].text

        lista.append(elem2)

    print(lista)

    if lista == ['26']:
        telegram_mensage(token, chat_id, estrategia5)

    if lista == ['3']:
        print('oo')

    if lista == ['25']:
        print('oo')

    if lista == ['8']:
        print ('Entrar no numero 32, 5, 14, 23')
        exit()

    if lista == ['22']:
        print ('Entrar no numero 32, 5, 14, 23')
        exit()
    if lista == ['23']:
        print ('Entrar no numero 32, 5, 14, 23')
    if lista == ['15']:
        print ('Entrar no numero 32, 5, 14, 23')
    if lista == ['12']:
        print ('Entrar no numero 32, 5, 14, 23')
    if lista == ['2']:
        print ('Entrar no numero 32, 5, 14, 23')
    if lista == ['21']:
        print ('Entrar no numero 32, 5, 14, 23')
    if lista == ['14']:
        print ('Entrar no numero 32, 5, 14, 23')

    if lista == ['6']:
        print ('Entrar no numero 32, 5, 14, 23')

    if lista == ['36']:
        print ('Entrar no numero 32, 5, 14, 23')

    if lista == ['5', '25']:
        print ('Entrar no numero 32, 5, 14, 23')



    if lista == ['32']:
        print ('Entrar no numero 23')
        break


    time.sleep(5)


