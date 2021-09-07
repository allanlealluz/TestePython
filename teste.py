from PySimpleGUI import PySimpleGUI as py
py.theme('dark')
layout = [
    [py.Text('0',key='valor',background_color='red')],
    [py.Text('Numero:'),py.Input(key='numero')],
    [py.Text('Porcentagem: '),py.Input(key='porc')],
    [py.Button('Calcular')]
]
janela = py.Window('Calculadora porc',layout)
while True:
    eventos,valores = janela.read()
    if eventos == py.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        porc = int(valores['porc']) / 100
        result = int(valores['numero']) * porc
        print(result)
        janela['valor'].update(result)





