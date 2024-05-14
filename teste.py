#Bibliotecas utilizadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
import os
from time import sleep

def main(url):
    #Prepara o navegador
    options = webdriver.ChromeOptions()
    options.use_chromium = False
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    actions = AC(driver)
    N1 = 6
    print('Entra no link desejado: '+url[:80])

    try:
        driver.get(url) 
        sleep(5)
        caminho = '/home/lucaires/Downloads'
        arquivo = driver.title
        arquivo_antigo = os.path.join(caminho,arquivo)
        arquivo_novo = arquivo_antigo.replace('.xlsx', ' (1).xlsx')

        print('Reconhece a página')
        driver.find_element(By.XPATH, '/html').send_keys(Keys.TAB)
        sleep(1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        sleep(2)

        for _ in range(N1):
            actions = actions.send_keys(Keys.TAB)
            actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print('Entrou em File')
        sleep(2)

        actions.send_keys(Keys.ARROW_DOWN)
        actions.pause(0.2)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.pause(0.2)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print('Entrou em Salvar')
        sleep(2)

        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        print('Baixou')
        sleep(8)
        driver.quit()

        print('\n'+arquivo_antigo)
        print(arquivo_novo)
        if os.path.exists(arquivo_antigo):
            print('Arquivo antigo existe, ou foi baixado pela primeira vez') 
            if os.path.exists(arquivo_novo):
                print('Arquivo novo baixado!')
                os.remove(arquivo_antigo)
                print('Arquivo antigo removido!')
                sleep(3)
                print('Arquivo novo renomeado!')
                os.rename(arquivo_novo, arquivo_antigo)

    except Exception as e:
        print(e)
    