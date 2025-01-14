import flet as ft


def main(page: ft.Page):
    page.title = ' Programa de relatório | Uber '
    page.bgcolor = '#130e16'
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def btn_edit(e):
        _stack_main.controls.clear()
        _stack_main.update()
        _stack_main.controls.append(_update)
        _stack_main.update()

    def btn_add(e):
        _stack_main.controls.clear()
        _stack_main.update()
        _stack_main.controls.append(_create)
        _stack_main.update()

    def btn_read(e):
        _stack_main.controls.clear()
        _stack_main.update()
        _stack_main.controls.append(_read)
        _stack_main.update()

    def btn_delete(e):
        _stack_main.controls.clear()
        _stack_main.update()
        _stack_main.controls.append(_delete)
        _stack_main.update()

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor='#acd3ff',
        shape=ft.NotchShape.CIRCULAR,
        height=60,
        padding=ft.Padding(left=0, right=0, bottom=0, top=0),
        content=ft.Row(
            controls=[
                ft.Container(expand=True),
                ft.IconButton(
                    icon_size=32,
                    icon=ft.icons.POST_ADD,
                    icon_color='#06142f',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#6c89a8',
                    tooltip='ADICIONAR CARD',
                    on_click=btn_add
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.CHROME_READER_MODE_OUTLINED,
                    icon_color='#06142f',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#6c89a8',
                    tooltip='LER CARD',
                    on_click=btn_read
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.EDIT_ROAD,
                    icon_color='#06142f',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#6c89a8',
                    tooltip='EDITAR CARD',
                    on_click=btn_edit
                ),
                ft.IconButton(
                    icon_size=28,
                    icon=ft.icons.DELETE_OUTLINE,
                    icon_color='#06142f',
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    bgcolor='#6c89a8',
                    tooltip='DELETAR CARD',
                    on_click=btn_delete
                ),
                ft.Container(expand=True)
            ]
        )
    )

    _main = ft.Container(
        width=400,
        height=550,
        border_radius=16,
        bgcolor='#060923',
        shadow=ft.BoxShadow(blur_radius=8, color='black'),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=16, right=16, bottom=16, top=16),
        content=ft.Text(
            value='Tela inicial',
            size=24,
            color=ft.colors.INDIGO_300)
    )

    _create = ft.Container(
        width=400,
        height=550,
        border_radius=16,
        bgcolor='#060923',
        shadow=ft.BoxShadow(blur_radius=8, color='black'),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=16, right=16, bottom=16, top=16),
        content=ft.Text(
            value='Tela de criação',
            size=24,
            color=ft.colors.INDIGO_300)
    )

    _read = ft.Container(
        width=400,
        height=550,
        border_radius=16,
        bgcolor='#060923',
        shadow=ft.BoxShadow(blur_radius=8, color='black'),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=16, right=16, bottom=16, top=16),
        content=ft.Text(
            value='Tela leitura',
            size=24,
            color=ft.colors.INDIGO_300)
    )

    _update = ft.Container(
        width=400,
        height=550,
        border_radius=16,
        bgcolor='#060923',
        shadow=ft.BoxShadow(blur_radius=8, color='black'),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=16, right=16, bottom=16, top=16),
        content=ft.Text(
            value='Tela ajustes',
            size=24,
            color=ft.colors.INDIGO_300)
    )
    
    controls = []
    controls.append(
            ft.Row(
                controls=[
                    # ft.ElevatedButton("Salvar", on_click=update_object),
                    ft.ElevatedButton("Voltar")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    _delete = ft.Container(
        width=400,
        height=550,
        border_radius=16,
        bgcolor='#060923',
        shadow=ft.BoxShadow(blur_radius=8, color='black'),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=16, right=16, bottom=16, top=16),
        content=ft.Text(
            value='Tela de exclusão',
            size=24,
            color=ft.colors.INDIGO_300)
    )

    _stack_main = ft.Stack(
        controls=[
            _main
        ]
    )

    page.add(_stack_main)
    page.update()


ft.app(target=main)
