from PySimpleGUI import PySimpleGUI as sg
from random import choice
import string

# Password options

lower = string.ascii_lowercase

upper = string.ascii_uppercase

digits = string.digits

specials = string.punctuation

password = ''

final = ''

# Layout
sg.theme('reddit')

layout = [
    [sg.Text('Password Options:'), sg.Checkbox('Digits', key='digits'), sg.Checkbox('Specials', key='specials'),
     sg.Checkbox('Lowercase', key='lower'), sg.Checkbox('Uppercase', key='upper')],
    [sg.Text('Number of characters:'), sg.Input(key='char_length', size=(8, 1)), sg.Text('Number of passwords:'),
     sg.Input(key='pass_quant', size=(8, 1))],
    [sg.Output(size=(70, 25), key='saida')],
    [sg.Button('Generate Password', button_color='green'), sg.Button('Clear'), sg.Button('Exit', button_color='red')]]

# Window
window = sg.Window('Password Generator by: @DygoBrks', layout)

# Events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Exit':
        break
    if events == 'Clear':
        password = ''
        window['saida'].update('')
    if events == 'Generate Password':
        password = ''
        if values['digits']:
            password += digits
        if values['specials']:
            password += specials
        if values['lower']:
            password += lower
        if values['upper']:
            password += upper
        window['saida'].update('')

        pass_quant = int(values['pass_quant'])
        pass_len = int(values['char_length'])

        for q in range(pass_quant):
            final = ''
            for i in range(pass_len):
                char = choice(password)
                final += char

            print()
            print(final)
