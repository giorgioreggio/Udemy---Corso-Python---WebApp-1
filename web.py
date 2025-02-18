import streamlit as st # Import Streamlit library to create Web App. Useful also for creating DataDashboard/Data Apps
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App") # title function
st.subheader("This is my todo app.")
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "Enter a to do: ", placeholder = "Add a new to do...",
              on_change=add_todo, key="new_todo") # label is a required argument
