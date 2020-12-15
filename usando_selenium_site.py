
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
#processo de logar na página
#função para ajudar a copiar e colar código
def achador_de_elemento(caminho):
    try:
        elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, caminho)))
        return elemento
    except:
        print('não achou elemento {}'.format(caminho))
        return None
#função para achar a foto no site ( está dando pau) Recebe um Xpath
def achador_de_foto(caminho):
    try:
        time.sleep(5)
        elemento = driver.find_elements_by_class_name(caminho)
        return elemento
    except:
        print('não achou elemento {}'.format(caminho))
        return None
#função para logar no site
def logador_site(site):
    try:
        usuario = achador_de_elemento('//*[@id="loginForm"]/div/div[1]/div/label/input')
        usuario.send_keys('pedromarcosgm@gmail.com')
        print('usuario é {}'.format(usuario))
        senha = achador_de_elemento('//*[@id="loginForm"]/div/div[2]/div/label/input')
        senha.send_keys('Shado123321')
        senha.send_keys(Keys.ENTER)
        achador_de_elemento('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        achador_de_elemento('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
        driver.get(site)
    except:
        print('já tá logado')
#Função de abrir o site desejado e perguntar ao usuário qual o nome da gostosa
def abridor_site_usuario(site_qualquer):
    # abrir o navegador
    #pergunta_ao_usuario = input('Digite o @ da pessoa gostosa que você quer:')
    pergunta_ao_usuario = 'anitta'
    #formar a palavra chave que vai para a pesquisa
    nome_escolhido = (site_qualquer + pergunta_ao_usuario)
    # navegar até o site
    driver.get(nome_escolhido)
    return nome_escolhido

driver = webdriver.Chrome()
site_formado = abridor_site_usuario('https://www.instagram.com/')
logador_site(site_formado)

try:
    #xpath = '//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div[3]/div[1]/a'
    #print('entrou ?')
    #imagem = achador_de_elemento(xpath)
    #imagem.click()
    driver.save_screenshot('fotinho_instagram.jpeg')
    #url = imagem.get_attribute("src")
    #urllib.request.urlretrieve(url, "fotinho_maneira.jpg")

except:
    print('deu erro')



time.sleep(5)

#driver.quit()






