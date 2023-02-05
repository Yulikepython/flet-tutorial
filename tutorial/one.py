import flet as ft

def main(page: ft.Page):
    page.add(
    ft.Row(controls=[
        ft.TextField(label="お名前"),
        ft.ElevatedButton(text="スタート")
    ])
)


ft.app(target=main)