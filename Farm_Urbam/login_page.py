import flet as ft
from main_page import MainPage
import jwt

ADMIN_PASSWORD = "123"
BACKGROUND_COLOR = "#1D3331"
BUTTON_COLOR = "#2C3E3F"
TEXT_COLOR_WHITE = ft.colors.WHITE
TEXT_COLOR_RED = ft.colors.RED
LOGO_PATH = "logo.png"

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = None
        self.password = None
        self.error_message = None
        

    def show(self):
        logo = ft.Image(src=LOGO_PATH, width=100, height=100)
        self.page.bgcolor = "#000000"

        self.username = ft.TextField(
            label="Login",
            width=300,
            height=40,
            text_style=ft.TextStyle(size=16)
        )
        self.password = ft.TextField(
            label="Senha",
            password=True,
            can_reveal_password=True,
            width=300,
            height=40,
            text_style=ft.TextStyle(size=16),
            on_submit=self.login_clicked
        )

        self.error_message = ft.Text(
            value="",
            color=TEXT_COLOR_RED,
            size=14,
            visible=False
        )

        login_button = ft.ElevatedButton(
            "Entrar",
            on_click=self.login_clicked,
            bgcolor=BUTTON_COLOR,
            color=TEXT_COLOR_WHITE,
            width=200,
            height=40,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                elevation=5,
            )
        )

        login_container = ft.Container(
            content=ft.Column(
                [
                    logo,
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    self.username,
                    self.password,
                    self.error_message,
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    login_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
            width=400,
            height=400,
            bgcolor=ft.colors.WHITE,
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center
        )

        self.page.clean()
        self.close_confirm_dialog()
        self.page.add(
            ft.Container(
                content=login_container,
                expand=True,
                alignment=ft.alignment.center,
                bgcolor=BACKGROUND_COLOR
            )
        )
        
    def close_confirm_dialog(self):
        # Fecha o diálogo de confirmação, se estiver aberto
        if self.page.dialog and self.page.dialog.open:
            self.page.dialog.open = False
            self.page.update()

    def login_clicked(self, e):
        # Verifica se os campos de usuário e senha estão preenchidos
        if not self.username.value or not self.password.value:
            self.error_message.value = "Por favor, preencha todos os campos."
            self.error_message.visible = True
            self.page.update()
            return  # Interrompe a execução se os campos estiverem vazios

        # Verifica se a senha está correta
        if self.password.value == ADMIN_PASSWORD:
            self.page.clean()
            main_page = MainPage(self.page)
            main_page.show()
        else:
            self.error_message.value = "Login ou senha incorretos. Tente novamente."
            self.error_message.visible = True
            self.page.update()
