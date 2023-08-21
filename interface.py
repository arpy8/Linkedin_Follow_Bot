import json
import PySimpleGUI as psg


def perm_var_set():
    def variable_app():
        psg.set_options(font=('Arial Bold', 16))
        psg.theme('Black')
        layout = [
            [psg.Text('Set login credentials')],
            [psg.Text('Gmail', size=(15, 1)), psg.Input(expand_x=False, size=(30, 1))],
            [psg.Text('Password', size=(15, 1)), psg.Input(expand_x=False, size=(30, 1))],
            [psg.OK('Enter', size=(6, 1)), psg.Cancel()]
        ]
        window = psg.Window('perma var setter', layout)
        event, values = window.read()
        window.close()
        return event, values

    values = variable_app()

    json_value = {
        "gmail": values[1][0],
        "password": values[1][1],
    }

    save_file = open("data.json", "w")
    json.dump(json_value, save_file, indent=6)
    save_file.close()