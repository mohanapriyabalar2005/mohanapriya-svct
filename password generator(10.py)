import PySimpleGUI as sg
import string
import random

# Function to generate a password
def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# GUI Layout
sg.theme('LightBlue')
layout = [
    [sg.Text('Password Generator', font=('Arial', 16))],
    [sg.Text('Password Length:'), sg.InputText(default_text='8', key='-LENGTH-', size=(5, 1))],
    [sg.Checkbox('Include Uppercase Letters', key='-UPPER-')],
    [sg.Checkbox('Include Numbers', key='-NUMBERS-')],
    [sg.Checkbox('Include Special Characters', key='-SPECIAL-')],
    [sg.Button('Generate'), sg.Button('Exit')],
    [sg.Text('Generated Password:'), sg.InputText(key='-OUTPUT-', size=(30, 1), readonly=True)]
]

# Create the Window
window = sg.Window('Password Generator', layout)

# Event Loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'Generate':
        try:
            length = int(values['-LENGTH-'])
            if length < 1:
                sg.popup('Password length must be greater than 0!')
                continue
            
            password = generate_password(
                length,
                values['-UPPER-'],
                values['-NUMBERS-'],
                values['-SPECIAL-']
            )
            window['-OUTPUT-'].update(password)
        except ValueError:
            sg.popup('Please enter a valid number for password length!')

window.close()

