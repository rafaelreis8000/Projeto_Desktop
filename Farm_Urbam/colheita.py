import flet as ft

class Colheita:
    def __init__(self):
        pass

    def get_content(self):
        # Aqui você pode definir a interface de gerenciamento de colheitas
        return ft.Column(
            [
                ft.Text("Gerenciamento de Colheitas", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.Text("Aqui você pode gerenciar suas colheitas."),
                # Adicione mais componentes conforme necessário
                ft.ElevatedButton("Adicionar Colheita", on_click=self.adicionar_colheita),
                ft.ElevatedButton("Listar Colheitas", on_click=self.listar_colheitas),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )

    def adicionar_colheita(self, e):
        # Lógica para adicionar uma nova colheita
        print("Adicionar uma nova colheita")

    def listar_colheitas(self, e):
        # Lógica para listar colheitas existentes
        print("Listar colheitas existentes")
