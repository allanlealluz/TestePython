import PySimpleGUI as py
from future.backports.email.quoprimime import header_check

py.theme('reddit')
layout = [
    [py.Text('Criar Personagem')],
    [py.Input(key='nome')],
    [py.Button('Cadastrar')]
]
janela = py.Window('Criar Personagem',layout)
while True:
    eventos,valores = janela.read()
    if eventos == py.WINDOW_CLOSED:
        break
    if eventos == 'Cadastrar':
        import conexao
        conexao.inserirPersonagem(valores['nome'])
        import Azatoh_Abilitys
        break
        

