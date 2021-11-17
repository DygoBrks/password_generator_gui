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

pass_list = []

# Layout
sg.theme('reddit')

layout = [
    [sg.Text('Password Options:'), sg.Checkbox('Digits', key='digits'), sg.Checkbox('Specials', key='specials'),
     sg.Checkbox('Lowercase', key='lower'), sg.Checkbox('Uppercase', key='upper')],
    [sg.Text('Number of characters:'), sg.Input(key='char_length', size=(8, 1)), sg.Text('Number of passwords:'),
     sg.Input(key='pass_quant', size=(8, 1))],
    [sg.Output(size=(70, 25), key='output')],
    [sg.Button('Generate', button_color='#0189ff'), sg.Button('Save', button_color='green', default_extension='.txt'), sg.Button('Clear', button_color='orange'), sg.Button('Exit', button_color='red')]]

# Window
window = sg.Window('Password Generator by: @TheHredric', layout)

# Events
while True:
    events, values = window.read()
    if events in (sg.WINDOW_CLOSED, 'Exit'):
        break

    elif events == 'Clear':
        password = ''
        window['output'].update('')

    elif events == 'Save':
        with open('password.txt', 'w') as f:
            for item in pass_list:
                f.write(item + '\n')

    elif events == 'Generate':
        pass_list = []
        password = ''
        if values['digits']:
            password += digits
        if values['specials']:
            password += specials
        if values['lower']:
            password += lower
        if values['upper']:
            password += upper
        window['output'].update('')

        pass_quant = int(values['pass_quant'])
        pass_len = int(values['char_length'])

        for q in range(pass_quant):
            final = ''

            for i in range(pass_len):
                char = choice(password)
                final += char

            print(f'{q + 1}: {final}\n')
            pass_list.append(final)
