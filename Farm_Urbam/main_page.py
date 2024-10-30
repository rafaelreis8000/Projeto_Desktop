import flet as ft
import asyncio

from usuarios import Usuarios
from cultura import Cultura
from plantio import Plantio
from colheita import Colheita
from insumo import Insumo
from fornecedor import Fornecedor
from pedido import Pedido
from relatorio import Relatorio
from home import Home

class MainPage:
    def __init__(self, page):
        self.page = page
        self.page.on_resize = self.resize_header

        # Instâncias das classes
        self.home_screen = Home()
        self.usuarios_screen = Usuarios()
        self.cultura_screen = Cultura()
        self.plantio_screen = Plantio()
        self.colheita_screen = Colheita()
        self.insumo_screen = Insumo()
        self.fornecedor_screen = Fornecedor()
        self.pedido_screen = Pedido()
        self.relatorio_screen = Relatorio()

    def resize_header(self, e):
        if self.page.window_width >= 1800:
            self.header.width = 1800
        else:
            self.header.width = self.page.window_width
        self.page.update()

    def show(self):
        self.page.clean()

        # Barra superior
        self.header = ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="logo2.png",
                        width=160,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.IconButton(
                        icon=ft.icons.LOGOUT,
                        icon_size=24,
                        tooltip="Sair",
                        icon_color=ft.colors.WHITE,
                        on_click=self.logout_clicked,
                        style=ft.ButtonStyle(padding=10, elevation=5)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                expand=True
            ),
            padding=0,
            bgcolor="#2C3E3F",
            width=self.page.window_width if self.page.window_width < 2300 else 1800
        )
        
#**************************************************************************************************
                                # Cria os botões da barra de menu
#**************************************************************************************************

        # Menu lateral com ícones
        menu_items = ft.Column(
            [
                self.menu_item("Home", ft.icons.HOME, self.menu_home_clicked),
                self.menu_item("Usuários", ft.icons.PERSON, self.menu_usuarios_clicked),
                self.menu_item("Culturas", ft.icons.NATURE, self.menu_culturas_clicked),
                self.menu_item("Plantios", ft.icons.NATURE_PEOPLE, self.menu_plantios_clicked),
                self.menu_item("Colheitas", ft.icons.ECO, self.menu_colheitas_clicked),
                self.menu_item("Insumos", ft.icons.INVENTORY, self.menu_insumos_clicked),
                self.menu_item("Fornecedores", ft.icons.SHOP, self.menu_fornecedores_clicked),
                self.menu_item("Pedidos", ft.icons.SHOPPING_CART, self.menu_pedidos_clicked),
                self.menu_item("Relatórios", ft.icons.ANALYTICS, self.menu_relatorios_clicked),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
        )

        sidebar = ft.Container(
            content=menu_items,
            bgcolor="#2E2E2E",
            padding=20,
            width=235,
            alignment=ft.alignment.top_left,
            border_radius=None
        )

        # Área central
        self.body = ft.Container(
            content=self.home_screen.get_content(),
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=None,
            expand=True
        )

        # Contêiner principal
        main_container = ft.Container(
            content=ft.Column(
                [
                    self.header,
                    ft.Row(
                        [
                            sidebar,
                            self.body
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    )
                ],
                spacing=0,
            ),
            expand=True,
            bgcolor="#000000",
            padding=0,
        )

        self.page.add(main_container)

    def menu_item(self, label, icon, click_event):
        # Função para criar itens de menu com ícones e estilização
        item_container = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, color=ft.colors.WHITE, size=24),
                    ft.Text(label, size=18, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=10,
            bgcolor="#2E2E2E",  # Cor de fundo padrão
            border_radius=0,  # Bordas arredondadas para melhor efeito visual
            on_hover=self.on_hover_menu_item,  # Evento de hover
            on_click=click_event  # Evento de clique
        )
        return item_container

    def on_hover_menu_item(self, e):
        # Altera a cor de fundo do item de menu ao passar o mouse
        e.control.bgcolor = "#151515" if e.data == "true" else "#2E2E2E"
        e.control.update()
        
#**************************************************************************************************
                             # faz o logout e chama a janela de alerta
#**************************************************************************************************

    def logout_clicked(self, e):
        # Diálogo de confirmação de saída
        confirm_dialog = ft.AlertDialog(
            title=ft.Text("Confirmação de Saída"),
            content=ft.Text("Você realmente deseja sair?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: self.close_dialog()),
                ft.ElevatedButton("Sair", on_click=self.confirm_exit)
            ]
        )

        # Configura o diálogo na página
        self.page.dialog = confirm_dialog
        self.page.dialog.open = True  # Abre o diálogo
        self.page.update()  # Atualiza a página para mostrar o diálogo
        
        
    async def confirm_exit(self, e):
    # Fecha o diálogo
        if self.page.dialog and self.page.dialog.open:
            self.page.dialog.open = False
            self.page.update()
            self.page.dialog = None

    # Aguardar um momento para garantir que o diálogo é completamente fechado
            await asyncio.sleep(0.1)

    # Navega para a tela de login
            self.show_login_screen()
    
    # Chama a função para exibir a tela de login
            self.show_login_screen()

    def close_dialog(self):
    # Mesmo procedimento para fechar e remover o diálogo
     if self.page.dialog and self.page.dialog.open:
        self.page.dialog.open = False
        self.page.update()
        self.page.dialog = None  # Remove o diálogo da página

    def show_login_screen(self):
      from login_page import LoginPage
      login_page = LoginPage(self.page)
      login_page.show()  # Mostra a tela de login
#**************************************************************************************************
                                # Chama as telas de menu
#**************************************************************************************************

    def menu_home_clicked(self, e):
        self.body.content = self.home_screen.get_content()
        self.page.update()

    def menu_usuarios_clicked(self, e):
        self.body.content = self.usuarios_screen.get_content()
        self.page.update()

    def menu_culturas_clicked(self, e):
        self.body.content = self.cultura_screen.get_content()
        self.page.update()

    def menu_plantios_clicked(self, e):
        self.body.content = self.plantio_screen.get_content()
        self.page.update()

    def menu_colheitas_clicked(self, e):
        self.body.content = self.colheita_screen.get_content()
        self.page.update()

    def menu_insumos_clicked(self, e):
        self.body.content = self.insumo_screen.get_content()
        self.page.update()

    def menu_fornecedores_clicked(self, e):
        self.body.content = self.fornecedor_screen.get_content()
        self.page.update()

    def menu_pedidos_clicked(self, e):
        self.body.content = self.pedido_screen.get_content()
        self.page.update()

    def menu_relatorios_clicked(self, e):
        self.body.content = self.relatorio_screen.get_content()
        self.page.update()
