import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"]=""


todos = functions.get_todos()

st.title("Planlama aplikasiyası")
st.subheader("Bu aplikasiyadan istifadə edərək gündəlik işlərinizi daha planlı idarə edə bilərsiniz.")
st.write("Tekst boşluğuna yeni planlarınızı yazın və Enter knopkasına klikləyin.\n"
         "Hərhansısa bir işi bitirdikdə isə planın qarşısında olan checkbox-a klikləyin həmin plan listdən silinəcək.")


st.text_input(label="Plan əlavə edin", placeholder="yeni planınızı əlavə edin...",
              on_change=add_todo, key='new_todo', value=st.session_state.get('new_todo', ''))

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


