# Local onde irá ficar todas as páginas do sistema
from page_objects import Page
from .elements import FazerLogin, AbrirLogin


class Login(Page):
    abrir_login = AbrirLogin()
    fazer_login = FazerLogin()