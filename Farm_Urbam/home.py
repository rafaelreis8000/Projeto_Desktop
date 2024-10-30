import flet as ft

class Home:
    def __init__(self):
        pass
    

    def get_content(self):
        # Aqui você pode definir a interface da tela inicial
        return ft.Column(
            [
                ft.Text("Bem-vindo ao Sistema de Gerenciamento da Fazenda Urbana", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.Text("Aqui você pode visualizar um resumo das operações."),
                ft.Text("Navegue pelas opções no menu para gerenciar as culturas, plantios, colheitas e mais."),
                # Você pode adicionar gráficos ou métricas aqui
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )
