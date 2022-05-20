from selenium import webdriver
from selenium.webdriver import Firefox, Chrome
from pages.page import Login
from dotenv import dotenv_values

credentials = dotenv_values(".env")


url = 'https://www.uber.com/br/pt-br/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(10)

        
login = Login(driver, url)
login.open()
login.abrir_login.abrir_menu()
login.fazer_login.logar(usuario=credentials["username"], senha=credentials["password"])

