import functionsDec
import FreeSimpleGUI as gi

label = gi.Text("Type in a to-do")
input_box = gi.InputText(tooltip="Enter a to-do", key='todo_input_box')
add_button = gi.Button("Add")
list_box = gi.Listbox(values=functionsDec.get_todos(), key='todos_listbox',
                      enable_events=True, size=(45, 10))
edit_button = gi.Button("Edit")

complete_button = gi.Button("Complete")

exit_button = gi.Button("Exit")

layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button],[exit_button]]

window = gi.Window("My To-do App", layout=layout, font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functionsDec.get_todos()
            new_todo = values['todo_input_box'] + "\n"
            todos.append(new_todo)
            functionsDec.write_todos(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input_box'].update(value='')

        case "Edit":
            todo_to_edit = values['todos_listbox'][0]
            edit_todo = values['todo_input_box']
            todos = functionsDec.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = edit_todo + "\n"
            functionsDec.write_todos(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input_box'].update(value='')

        case "Complete":
            todo_to_complete = values['todos_listbox'][0]
            todos = functionsDec.get_todos()
            todos.remove(todo_to_complete)
            print(todos)
            functionsDec.write_todos(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input_box'].update(value='')

        case 'todos_listbox':
            window['todo_input_box'].update(value=values['todos_listbox'][0].strip("\n"))

        case 'Exit':
            break

        case gi.WIN_CLOSED:
            break

window.close()
