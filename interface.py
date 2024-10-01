import functionsDec
import FreeSimpleGUI as gi

label = gi.Text("Type in a to-do")
input_box = gi.InputText(tooltip="Enter a to-do")
add_button = gi.Button("Add")

window = gi.Window("My To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
