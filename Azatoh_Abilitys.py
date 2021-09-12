import conexao
import PySimpleGUI as py
py.theme('reddit')
dados = conexao.SelecionarPersonagens()
valor = []
for data in dados:
    valor.append(data[1])
layout = [
    [py.Text('Azaroth Abilitys')],
    [py.OptionMenu(valor,default_value='Selecione')],
    [py.Text('Nome da habilidade'),py.Input(key='nomehab')],
    [py.Text('Descrição'),py.Input(key='hab')],
    [py.Button('Cadastrar')]
]
janela = py.Window('Azaroth Ability',layout)
while True:
    eventos,valores = janela.read()
    if eventos == py.WINDOW_CLOSED:
        break
    if eventos == 'Cadastrar':
        t = valores[0]
        conexao.inserir(t,valores['nomehab'],valores['hab'])
        janela.Close()
        py.popup('Hello',t)

