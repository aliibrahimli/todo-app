FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# Exercise for day 14 below
# FREEZING_POINT = 0
# BOILING_POINT = 100


# def water_state(temperature):
#    if temperature <= FREEZING_POINT:
#        return "Solid"
#    elif FREEZING_POINT < temperature < BOILING_POINT:
#        return "Liquid"
#    else:
#        return "Gas"
