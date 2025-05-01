from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time


chrome_driver = "C:\Program Files\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)


url = 'https://www.imdb.com/chart/top/'
driver.get(url)
time.sleep(2)


dic = {
    'titulo': [],
    'ano':[]
}

pagina_atual = 1

try:
    WebDriverWait(driver, 2).until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, 'ipc-metadata-list-summary-item'))
    )
    print('Filmes encontrados!')
except Exception as e:
    print('Filmes não encontrados!', e)

filmes = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')

for filme in filmes:
    try:
        titulo = filme.find_element(By.CSS_SELECTOR,'[class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-143a3ae8-2 ezwMlU cli-title with-margin"]').text.strip()
        ano_e_classificacao = filme.find_element(By.CSS_SELECTOR,'[class="sc-5179a348-6 bnnHxo cli-title-metadata"]').text.strip()
#
        dic['titulo'].append(titulo)
        dic['ano'].append(ano_e_classificacao)

        print(f'dados coletados.')
    except Exception as e:
        print('erro ao coletar os dados', e)
#
df = pd.DataFrame(dic)
df.to_excel('imdbWebScraping.xlsx', index= False)