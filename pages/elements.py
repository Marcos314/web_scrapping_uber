from time import sleep

from abc import ABC
from selenium.webdriver.common.by import By
from page_objects import PageElement
from page_objects.page_objects import Page

class AbrirLogin(PageElement):
    sub_menu_locator = (By.XPATH,"/html/body/div[1]/div/div/div[1]/main/nav/div/ul[4]/li[4]/button")
    botao_login_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[4]/section/div/div/div/div/div[3]/a/div[2]/h2')


    def abrir_menu(self):
        sleep(2)
        self.find_element(self.sub_menu_locator).click()
        sleep(2)
        self.find_element(self.botao_login_locator).click()

    
class FazerLogin(PageElement):

    username = (By.ID, "mobile")
    password = (By.ID, "password")
    mensagem = (By.ID, "smsOTP")
    btn_avancar = (By.ID, "next-button")


    rede_social = (By.TAG_NAME, 'a')
    google = (
        By.XPATH, '/html/body/div[1]/div/div/div/div/div/a[2]/div/div[2]')
    janela = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    user_google = (By.ID, 'identifierId')
    pass_google = (By.ID, 'pass')


    facebook = (
        By.XPATH, '/html/body/div[1]/div/div/div/div/div/a[1]/div/div[2]')
    user_face = (By.ID, 'email')
    pass_face = (By.ID, 'pass')
    btn_face = (By.ID, "loginbutton")
    
    btn_login = (By.ID, "loginbutton")

    def login_mobile(self, phone, password):
        self.find_element(self.username).send_keys(phone)
        self.find_element(self.btn_avancar).click()
        sleep(10)
        self.find_element(self.password).send_keys(password)

    def logar_mobile(self, phone, password):
        self.login_mobile(phone, password)
    
    def login_with_google(self, email, password):
        self.find_element(self.rede_social).click()
        sleep(1)
        self.find_element(self.google).click()
        sleep(1)        
        self.find_element(self.user_google).send_keys(email)
        sleep(1)        
        self.find_element(self.pass_google).send_keys(password)
        sleep(1)
        self.find_element(self.botao_login).click()

    def logar_google(self, email, password):
        self.login_with_google(email, password)
    
    def login_facebook(self, usuario, senha):
        self.find_element(self.rede_social).click()
        sleep(1)
        self.find_element(self.facebook).click()
        sleep(1)
        self.find_element(self.user_face).send_keys(usuario)
        sleep(1)
        self.find_element(self.pass_face).send_keys(senha)
        sleep(1)
        self.find_element(self.btn_face).click()

    def logar(self, usuario: str, senha: str):
        self.login_facebook(usuario, senha)

