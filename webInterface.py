import os
import streamlit as st
import functionsDec

todos = functionsDec.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functionsDec.write_todos(todos)
    st.session_state["rerun_flag"] = not st.session_state["rerun_flag"]


# Initialize rerun_flag in session_state if it doesn't exist
if "rerun_flag" not in st.session_state:
    st.session_state["rerun_flag"] = False

st.title("My To-Do App")
st.subheader("This is my to-do app")

# Create a temporary list to track items to remove
todos_to_remove = []

# Iterate over a copy of todos to avoid index shifting
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")  # Use unique keys based on index
    if checkbox:
        todos_to_remove.append(index)  # Mark the index for removal
        del st.session_state[f"todo_{index}"]

# Apply the changes to todos after the loop
if todos_to_remove:
    for index in sorted(todos_to_remove, reverse=True):
        todos.pop(index)
    functionsDec.write_todos(todos)
    st.session_state["rerun_flag"] = not st.session_state["rerun_flag"]  # Trigger rerun after changes

# Text input for adding new todos
st.text_input(label="hi", placeholder="Add a new to-do",
              on_change=add_todo, key='new_todo', label_visibility='hidden')
