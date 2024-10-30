import flet as ft

class Fornecedor:
    def __init__(self):
        pass

    def get_content(self):
        # Aqui você pode definir a interface de gerenciamento de fornecedores
        return ft.Column(
            [
                ft.Text("Gerenciamento de Fornecedores", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.Text("Aqui você pode gerenciar seus fornecedores."),
                # Adicione mais componentes conforme necessário
                ft.ElevatedButton("Adicionar Fornecedor", on_click=self.adicionar_fornecedor),
                ft.ElevatedButton("Listar Fornecedores", on_click=self.listar_fornecedores),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )

    def adicionar_fornecedor(self, e):
        # Lógica para adicionar um novo fornecedor
        print("Adicionar um novo fornecedor")

    def listar_fornecedores(self, e):
        # Lógica para listar fornecedores existentes
        print("Listar fornecedores existentes")
