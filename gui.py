import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("DarkGreen3")

clock = sg.Text('', key='clock')
label = sg.Text("Yeni plan əlavə et:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Əlavə et", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Redaktə et")
complete_button = sg.Button("Sil")
exit_button = sg.Button("Çıxış")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('Planlama aplikasiyası',
                   layout=layout,
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case "Əlavə et":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            if values['todo'] == "":
                sg.popup("Zəhmət olmasa nəsə yazın...",font=("Helvetica", 10))
            else:
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case "Redaktə et":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Zəhmət olmasa listdə olanlardan birini seçin.", font=("Helvetica", 10))
            except ValueError:
                sg.popup("List boşdur...", font=("Helvetica", 10))
        case "Sil":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Zəhmət olmasa listdə olanlardan birini seçin.", font=("Helvetica", 10))
            except ValueError:
                sg.popup("List boşdur. Zəhmət olmasa yeni plan əlavə edin", font=("Helvetica", 10))

        case 'Çıxış':
            break
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("List boşdur...", font=("Helvetica", 10))

        case sg.WIN_CLOSED:
            try:
                break
            except TypeError:
                sg.popup('Çıxış etmək üçün "Çıxış" düyməsinə klik edin ')

window.close()
