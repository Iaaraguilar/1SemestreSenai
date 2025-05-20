#pip install selenium
#selenium vai simular como se a gente estivesse no site
#Modulo para controlar o navegador
from selenium import webdriver
#trabalhar com dataframe
import pandas as pd
#Localizador de elementos
from selenium.webdriver.common.by import By 

#servico para configurar o caminho de excutavel do chromerdriver
from selenium.webdriver.chrome.service import Service
#Cria classe que permite executar acoes avancadas(o mover do mouse, clique e arrasta etc...)
from selenium.webdriver.common.action_chains import ActionChains

#a classe que espeera de forma explicita ate que uma condicao seja satisfeita(que um elemento apareca)
from selenium.webdriver.support.ui import WebDriverWait
 
#condicoes esperadas usadas com o webdriverWait
from selenium.webdriver.support import expected_conditions as ec

#uso de funcoes relacionadas
import time
#uso de tratamento de excecao
from selenium.common.exceptions import TimeoutException

#definir o caminho do crhome driver
chrome_driver= r'C:\Program Files\chromedriver-win64\chromedriver.exe' #Simular o drive

service=Service(chrome_driver)#iniciar o navegador
options=webdriver.ChromeOptions()#configurar as opcoes do navegador
#options.add_argument('--headless')#sem interface visual
options.add_argument("--disable-gpu")#evitar possiveis erros graficos
options.add_argument("--window-size=1920,1080")#define uma resolucao fixa
#------------------------------------------------------------------------------------


#iniciar o webdriver
driver=webdriver.Chrome(service=service, options=options)

#URL INICIAL
url_base='https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
driver.get(url_base)#vai executar 
time.sleep(5)#aguarda 5 segundos para garantir que a pagina carregue

#criar um dicionario vazio para armazenar as marcas e os precos das cadeiras
dic_produtos={'marca':[],'preco':[]}
#vamos iniciar na pagina 1 e incrementamos a cada troca de pagina
pagina=1

#PADRAO
while True:
   print(f"\n Coletando dados da pagina {pagina}...")
    #responsavel por achar
   try:
     #cria uma espera de ate 10 segundos 
     #until(...), faz com que o codigo espere ate que a condicao seja verdadeira
      WebDriverWait(driver,10).until(
        #ele verifica se todos os elementos productCard estao acessiveis
        #BY- indica que a busca sera feita atraves da classe CSS
        ec.presence_of_all_elements_located((By.CLASS_NAME,"productCard"))#seletor de classes e do CSS
      )
      print("Elementos encontrados com sucesso")
   except TimeoutException:
       print("Tempo de espera excedido") 


   produtos= driver.find_elements(By.CLASS_NAME,"productCard")
   for produto in produtos:
      try:
         nome = produto.find_element(By.CLASS_NAME,'nameCard').text.strip()
         preco=produto.find_element(By.CLASS_NAME,'priceCard').text.strip()

         print(f'{nome}-{preco}')
         dic_produtos['marca'].append(nome)
         dic_produtos['preco'].append(preco)
      except Exception:
         print('Erro ao coletar dados:',Exception)

 #encontrar o acesso para a proxima pagina 
   try:
      botaoproximo= WebDriverWait(driver,5).until(
         ec.element_to_be_clickable((By.CLASS_NAME,"nextLink"))#passar para a proxima pagina
      )

      if botaoproximo:
         driver.execute_script('arguments[0].scrollIntoView();',botaoproximo)
         time.sleep(1)
         #clicar na seta da proxima pagina
         driver.execute_script('arguments[0].click();',botaoproximo)
         pagina +=1
         print(f"indo para a pagina{pagina}")
         time.sleep(5)
      else:
         print("voce chegou na ultima pagina")
         
   except Exception as e:
      print("Erros ao encontrar as paginas",e)
      break
      
# fechar o navegador

driver.quit()
df=pd.DataFrame(dic_produtos)
df.to_excel("Cadeiras gamers.xlsx",index=False)
print(f"Arquivo cadeiras salvo com sucesso{len(df)} produtos capturados")






