def solution():
    # Define the initial number of notebooks Jack and Gerald have
    gerald_notebooks = 8
    jack_notebooks = gerald_notebooks + 13

    # Update the number of notebooks after Jack gives some away
    jack_notebooks -= 5
    jack_notebooks -= 6

    result = jack_notebooks
    return result

print(solution())