import flet as ft

class Usuarios:
    def __init__(self):
        self.users = []  # Lista para armazenar usuários
        self.form_visible = False  # Flag para controlar a visibilidade do formulário

    def get_content(self):
        """Retorna o conteúdo da página."""
        if self.form_visible:
            return self.create_registration_form()  # Exibe o formulário se a flag estiver ativa
        else:
            return self.create_user_management()  # Exibe a tela de gerenciamento de usuários

    def create_user_management(self):
        """Método para criar a interface inicial de gerenciamento de usuários."""
        return ft.Column(
            [
                ft.Text("Gerenciamento de Usuários", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.ElevatedButton(
                    text="Clique Aqui",
                    on_click=self.show_form  # Chama o método para exibir o formulário ao clicar
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )

    def show_form(self, e):
        """Método para exibir o formulário de cadastro e limpar a área central."""
        self.form_visible = True  # Define a flag para mostrar o formulário
        e.page.update()  # Atualiza a página para refletir as mudanças

    def create_registration_form(self):
        """Método para criar o formulário de cadastro."""
        return ft.Column(
            [
                ft.Text("Formulário de Cadastro", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20),
                ft.TextField(label="Nome", autofocus=True),
                ft.TextField(label="Email"),
                ft.TextField(label="Senha", password=True),
                ft.ElevatedButton(text="Cadastrar", on_click=self.register_user),  # Botão de cadastro
                ft.ElevatedButton(text="Voltar", on_click=self.go_back)  # Botão para voltar
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )

    def register_user(self, e):
        """Método para registrar o usuário (pode ser expandido com a lógica de registro)."""
        # Aqui você pode adicionar a lógica para registrar o usuário
        print("Usuário cadastrado!")  # Simulação de registro

    def go_back(self, e):
        """Método para voltar à tela de gerenciamento de usuários."""
        self.form_visible = False  # Define a flag para esconder o formulário
        e.page.update()  # Atualiza a página para refletir as mudanças

# Para executar o aplicativo
if __name__ == "__main__":
    app = Usuarios()
    ft.app(target=app.get_content)
