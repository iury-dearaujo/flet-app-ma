import flet as ft


def main(page: ft.Page):
    page.title = ' Programa de relatório | Uber '
    page.bgcolor = '#130e16'
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#ffe4ac',
        shape=ft.NotchShape.AUTO,
        content=ft.Row(
            controls=[
                ft.Container(expand=True),
                ft.IconButton(
                    icon_size=34,
                    icon=ft.icons.HOME_MAX,
                    icon_color='#4c0909',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#a17156',
                    tooltip='MENU PRINCIPAL'
                ),
                ft.IconButton(
                    icon_size=32,
                    icon=ft.icons.POST_ADD,
                    icon_color='#4c0909',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#a17156',
                    tooltip='ADICIONAR CARD'
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.CHROME_READER_MODE_OUTLINED,
                    icon_color='#4c0909',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#a17156',
                    tooltip='LER CARD'
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.EDIT_ROAD,
                    icon_color='#4c0909',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#a17156',
                    tooltip='EDITAR CARD'
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.DELETE_OUTLINE,
                    icon_color='#4c0909',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#a17156',
                    tooltip='DELETAR CARD'
                ),
                ft.Container(expand=True)
            ]
        )
    )

    # _stack_main = ft.Stack(
    #     controls=[
    #
    #     ]
    # )

    page.update()


ft.app(target=main)
