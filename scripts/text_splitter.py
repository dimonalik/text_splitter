import PySimpleGUI as sg
splitted = ""
text = ""
sg.theme('DarkBlue4')
layout = [[sg.Text('Сюди текст для розділення'), sg.InputText(size=(20, 5), key='input')],
            [sg.Text('На скільки знаків ділимо?'),sg.InputText(size=(5, 1), key='symbols'),sg.Text('(Враховуйте додаткові символи на кількість постів)')],
            [sg.Checkbox('Додавати кількість постів?', key='split')], 
            [sg.Button('Розчленити')],
            [sg.Multiline(splitted, key='-logtext-', size =(None, 10), rstrip=False)], [sg.Button('Очистити'), sg.Text('                                                © @uahave.fun', text_color='dark blue', font=('Helvetica', 10), justification='right')],[sg.Text('------------------------------------------------------')],[sg.Button('Закрити')]
            ]

window = sg.Window('Розділяч', layout)

while True:
    event, values = window.read()
    if event in (None, 'Закрити'):
        break
    if event == 'Розчленити':
        if values['input'] == '':
            sg.popup('Введіть текст!')
            continue
        if values['symbols'].isdigit() == False:
            sg.popup('Введіть кількість символів цифрами!')
            continue
        if values['symbols'] == '':
            sg.popup('Введіть кількість символів!')
            continue
        if int(values['symbols']) < 1:
            sg.popup('Введіть кількість символів більше 0!')
            continue
        if int(values['symbols']) > len(values['input']):
            sg.popup('Введіть кількість символів менше довжини тексту!')
            continue
        if int(values['symbols']) == len(values['input']):
            sg.popup('Введіть кількість символів менше довжини тексту!')
            continue
        es = [values['input'][i:i + int(values['symbols'])] for i in range(0, len(values['input']), int(values['symbols']))] 
        for i in es:
            if values['split'] == True:
                text =  text + str(es.index(i)+1) + '/' + str(len(es))+ ' ' + splitted + i +  '\n' + '\n'
            else:
                text = text + splitted + i + '\n' + '\n'
        window['-logtext-'].update(text)
    if event == 'Очистити':
        window['-logtext-'].update('')
        text = ''
window.close()

