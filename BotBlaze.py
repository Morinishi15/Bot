import time
from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#######################################

######### Por informações do seu bot.########
api_key = '5619862462:AAEkDj4ksz5rgMP4CaK_IHArYlqFSl688JA'  # TOKEN DO SEU BOT
chat_id = '-837954839' # ID DO CANAL pladix
#####################################
bot = telebot.TeleBot(token=api_key)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')

analisar = 0
gale_atual = 0
analisar_open = 0
resultsDouble = []

while True:
    def qualnum(x):
        if x == '0':
            return 0

        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14
    def qualcor(x):
        if x == '0':
            return 'B'

        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'Vermelho'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'Preto'
       
    try: 
        resulROOL = nav.find_element(
        By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        print(erro)
        print('ERRO 403')
    except Exception as erro:
        print('ERRO 404')


    analisar_open = 0
    if resulROOL == 'Girando...':
        analisar_open = 1
        print('Analisando')
        time.sleep(13) 
        c = nav.page_source
        resultsDouble.clear()
        
        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                resultsDouble.append(i.getText())
            else:
                resultsDouble.append('0')
        
        resultsDouble = resultsDouble[:-1]
        
        if analisar_open == 1:

            default = resultsDouble[0:3]

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            finalnum = list(mapeando)
            finalcor = list(mapeando2) 


            def CHECK_VERSION(num):
                global analisar
                global gale_atual
                

                if analisar == 0:
                    if num == ['Vermelho', 'P', 'P']:
                        analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
POSSÍVEL ENTRADA NO 🟥 VERMELHO
SUGERIMOS PROTEGER NO ⬜️ BRANCO
💻 BONUS BLAZE DOUBLE                    
                        ''')
                        return
                    if num == ['Preto', 'V','V']:
                        analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
POSSÍVEL NO 🟥 VERMELHO
SUGERIMOS PROTEGER NO ⬜️ BRANCO
💻 BONUS BLAZE DOUBLE
                        ''')
                        return

                elif analisar == 1:
                   
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['P', 'Vermelho', 'P']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
                            ENTRADA CONFIRMADA NO 🟥 VERMELHO
                            SUGERIMOS PROTEGER NO ⬜️ BRANCO
                        ''')
                            return
                        if num == ['P', 'Preto', 'V']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
                            ENTRADA CONFIRMADA NO 🟥 VERMELHO
                            SUGERIMOS PROTEGER NO ⬜️ BRANCO
                        ''')
                            return
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['V or Vermelho', 'P', 'Vermelho']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
✳️✳️💎GREEEEEEEEEEEEEENNNNNNNN💎✳️✳️
                        ''')
                            return
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['V or Vermelho', 'P', 'Preto']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
✳️✳️💎GREEEEEEEEEEEEEENNNNNNNN💎✳️✳️
                        ''')
                            return
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['B', 'P', 'Vermelho']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
✳️✳️💎GREEEEEEEEEEEEEENNNNNNNN💎✳️✳️
                        ''')
                            return
                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['B', 'P', 'Preto']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
✳️✳️💎GREEEEEEEEEEEEEENNNNNNNN💎✳️✳️
                        ''')
                            return
                        if num == ['P', 'P', 'Vermelho']:
                            gale_atual = gale_atual+1
                            bot.send_message(chat_id=chat_id, text='''
Vamos para o GALE 1
                        ''')
                            return
                        if num == ['P', 'P', 'Preto']:
                            gale_atual = gale_atual+1
                            bot.send_message(chat_id=chat_id, text='''
Vamos para o GALE 1
                        ''')
                            return

                    if gale_atual == 1:
                        if num == ['V or Vermelho' ,'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
WIN GALE 1✅
                        ''')
                            return

                        if num == ['B', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
BRANCO GALE 1⚪️
                        ''')
                            return


                        if num == ['P', 'P', 'P']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=chat_id, text='''
LOSS 🔴
                        ''')
                            return
                        

            checkVersion = CHECK_VERSION(finalcor)
            print(checkVersion)