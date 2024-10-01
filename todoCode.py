# from functionsDec import get_todos, write_todos
import functionsDec
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("The time is: ", now)

while True:

    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete "
                        "or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functionsDec.get_todos()
        todos.append(todo)
        functionsDec.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functionsDec.get_todos()
        # new_todos = [item.strip('\n') for item in todos] -->solution to remove break line  or /n  from the text
        # file using list comprehension

        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functionsDec.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            functionsDec.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

            continue

    elif user_action.startswith("exit"):
        break;

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])
            todos = functionsDec.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functionsDec.write_todos(todos)
            message = f"Todo {todo_to_remove.title()} was removed from the list."
            print(message)

        except IndexError:
            print(f"There is no item with index {number}")

            continue

    else:
        print("Invalid command")

print("Bye")
