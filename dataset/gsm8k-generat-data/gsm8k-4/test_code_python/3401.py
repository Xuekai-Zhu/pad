def solution():
    """Jack says he has 13 more notebooks in his bag than Gerald. Jack gives 5 notebooks to Paula and 6 notebooks to Mike. If Gerald has 8 notebooks, how many notebooks does Jack have left?"""
    # Define the number of notebooks Gerald has
    gerald_notebooks = 8

    # Calculate the number of notebooks Jack has
    jack_notebooks = gerald_notebooks + 13

    # Subtract the number of notebooks Jack gives away
    jack_notebooks -= 5
    jack_notebooks -= 6

    result = jack_notebooks
    return result

print(solution())