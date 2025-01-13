import json
import flet as ft

from JsonUtils import JsonUtils
from datetime import datetime

data = []


class ObjectItem:
    def __init__(self):
        self.objeto = None
        self.objetos = []
        self.initObj()

    def initObj(self):
        self.objeto = {"ID": None, "Data atual": None, "Receita": None, "KM rodada": None}

    def newObject(self):
        self.initObj()
        return self.objeto


def main(page: ft.Page):
    page.title = "Simple App with ObjectItem"
    page.window.width = 400
    page.window.height = 300
    page.theme_mode = ft.ThemeMode.LIGHT

    object_item = ObjectItem()
    json_utils = JsonUtils()

    def updateData():
        global data
        try:
            with open("../../report.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("\tErro: O arquivo 'report.json' não foi encontrado.")
        except json.JSONDecodeError:
            print("\tErro: O arquivo 'report.json' não é um JSON válido.")

    def voltar_ao_menu(e):
        page.views.clear()
        page.views.append(menu_view())
        page.update()

    def adicionar_objeto_view():
        new_obj = object_item.newObject()
        text_fields = {}

        openCalendar = ft.ElevatedButton(
            text=' ',
            icon=ft.icons.CALENDAR_MONTH,
            color=ft.colors.BLACK,
            on_click=lambda e: page.open(calendar),
            width=44
        )



        def update_object(e):
            for key, text_field in text_fields.items():
                object_item.objeto[key] = text_field.value

            json_utils.update_jsn(object_item.objeto)
            updateData()
            data_log_str = f"data = {object_item.objeto}"

            log_textbox = ft.TextField(
                label="Log",
                value=data_log_str,
                disabled=True,
                width=280,
                height=600,
                multiline=True
            )

            controls.append(log_textbox)
            page.views[-1].controls = controls
            page.update()

        controls = [
            ft.Text("Adicionar Objeto", size=24, weight="bold", text_align=ft.TextAlign.CENTER)
        ]

        def change(e):
            calendar_text_field.value = f"{e.control.value.strftime('%d/%m/%y')}"
            calendar_text_field.update()

        for key in new_obj.keys():
            if key.lower().find("data") != -1:
                calendar = ft.DatePicker(
                    first_date=datetime(year=1900, month=1, day=1),
                    last_date=datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day),
                    on_change=change,
                    on_dismiss=None
                )
                calendar_text_field = ft.TextField(
                    label=key,
                    width=150,
                    value=None,
                    on_change=lambda e: print(f"{e.control.value}"),
                    disabled=True
                )
                controls.extend([
                    ft.Row(
                        controls=[
                            ft.Text(f"{key}:", size=16, width=86),
                            openCalendar,
                            calendar_text_field
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ])
            elif key == 'ID':
                text_field = ft.TextField(label=key, width=202, value=str(len(object_item.objetos)), disabled=True)
                text_fields[key] = text_field
                controls.extend([
                    ft.Row(
                        controls=[
                            ft.Text(f"{key}:", size=16, width=86),
                            text_field
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ])
            else:
                text_field = ft.TextField(label=key, width=202)
                text_fields[key] = text_field
                controls.extend([
                    ft.Row(
                        controls=[
                            ft.Text(f"{key}:", size=16, width=86),
                            text_field
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ])

        controls.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton("Salvar", on_click=update_object),
                    ft.ElevatedButton("Voltar", on_click=voltar_ao_menu)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        page.views.append(
            ft.View(
                "add_object",
                controls=controls,
                vertical_alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            )
        )
        page.update()

    # Menu principal
    def menu_view():
        return ft.View(
            "menu",
            controls=[
                ft.Text("Menu", size=32, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton("Add Object", on_click=lambda e: adicionar_objeto_view()),
                ft.ElevatedButton("Del Object", on_click=lambda e: abrir_tela("Del Object")),
                ft.ElevatedButton("Alter Object", on_click=lambda e: abrir_tela("Alter Object")),
                ft.ElevatedButton("Read Object", on_click=lambda e: abrir_tela("Read Object")),
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def abrir_tela(titulo):
        page.views.append(
            ft.View(
                f"tela_{titulo}",
                controls=[
                    ft.Text(titulo, size=24, weight="bold", text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton("Back", on_click=voltar_ao_menu),
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    page.views.append(menu_view())
    page.update()


ft.app(target=main)
