def solution():
    """Jack says he has 13 more notebooks in his bag than Gerald. Jack gives 5 notebooks to Paula and 6 notebooks to Mike. If Gerald has 8 notebooks, how many notebooks does Jack have left?"""
    # Define the initial number of notebooks Jack has
    jack_start = 8 + 13

    # Jack gives 5 notebooks to Paula
    jack_after_paula = jack_start - 5

    # Jack gives 6 notebooks to Mike
    jack_remaining = jack_after_paula - 6

    # Display the number of notebooks Jack has left
    result = jack_remaining
    return result

print(solution())