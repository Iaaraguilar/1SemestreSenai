from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import TimeoutException
chrome_driver= r'C:\Program Files\chromedriver-win64\chromedriver.exe' 
service=Service(chrome_driver)
options=webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

drive=webdriver.Chrome(service=service,options=options)
meulink='https://www.kabum.com.br/perifericos/gabinetes'
drive.get(meulink)
time.sleep(5)

dicionario={'marca':[], 'preco':[]}

pagina=1
while True:
   print(f"\n Coletando dados da pagina {pagina}...")
 
   try:
 
      WebDriverWait(drive,10).until(
     
        ec.presence_of_all_elements_located((By.CLASS_NAME,"productCard"))
      )
      print("Elementos encontrados com sucesso")
   except TimeoutException:
       print("Tempo de espera excedido") 


   produtos= drive.find_elements(By.CLASS_NAME,"productCard")
   for produto in produtos:
      try:
         nome = produto.find_element(By.CLASS_NAME,'nameCard').text.strip()
         preco=produto.find_element(By.CLASS_NAME,'priceCard').text.strip()

         print(f'{nome}-{preco}')
         dicionario['marca'].append(nome)
         dicionario['preco'].append(preco)
      except Exception:
         print('Erro ao coletar dados:',Exception)


   try:
      botaoproximo= WebDriverWait(drive,5).until(
         ec.element_to_be_clickable((By.CLASS_NAME,"nextLink"))
      )

      if botaoproximo:
         drive.execute_script('arguments[0].scrollIntoView();',botaoproximo)
         time.sleep(1)
        
         drive.execute_script('arguments[0].click();',botaoproximo)
         pagina += 1
         print(f"indo para a pagina: {pagina}")
         time.sleep(5)
      else:
         print("voce chegou na ultima pagina")
         
   except Exception as e:
      print("Erros ao encontrar as paginas",e)
      break
      

drive.quit()
df=pd.DataFrame(dicionario)
df.to_excel("Gabinetes.xlsx",index=False)
print(f"Arquivo dos Gabinetes salvos com sucesso{len(df)} produtos capturados")