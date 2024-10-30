# main.py

import flet as ft
from login_page import LoginPage

def main(page: ft.Page):

    page.title = "Sistema de Gerenciamento da Fazenda Urbana"
    page.vertical_scroll = ft.ScrollMode.AUTO
    page.horizontal_scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Configura o app para abrir em tela cheia
    #page.window.full_screen = True
    page.window.maximized = True

    login_page = LoginPage(page)
    login_page.show()

if __name__ == "__main__":
    ft.app(target=main)
