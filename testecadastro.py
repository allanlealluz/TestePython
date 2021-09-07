from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha '),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o Login? ')],
    [sg.Button('Entrar')]
]
layout2 = [[sg.Text('Opa você conseguiu logar')]]
janela = sg.Window('Tela de Login',layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
       break
    if eventos == 'Entrar':
        if valores['usuario'] == 'jhonathan' and valores['senha'] == '123456':
            janela.Close()
            janela2 = sg.Window('Opa compatriota',layout2)
while True:
    eventos, valores = janela2.read()
    if eventos == sg.WINDOW_CLOSED:
        break
