import flet as ft

class Insumo:
    def __init__(self):
        pass

    def get_content(self):
        # Aqui você pode definir a interface de gerenciamento de insumos
        return ft.Column(
            [
                ft.Text("Gerenciamento de Insumos", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.Text("Aqui você pode gerenciar seus insumos."),
                # Adicione mais componentes conforme necessário
                ft.ElevatedButton("Adicionar Insumo", on_click=self.adicionar_insumo),
                ft.ElevatedButton("Listar Insumos", on_click=self.listar_insumos),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )

    def adicionar_insumo(self, e):
        # Lógica para adicionar um novo insumo
        print("Adicionar um novo insumo")

    def listar_insumos(self, e):
        # Lógica para listar insumos existentes
        print("Listar insumos existentes")
