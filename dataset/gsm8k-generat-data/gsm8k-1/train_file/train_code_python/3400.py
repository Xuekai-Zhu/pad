def solution():
    """Jack says he has 13 more notebooks in his bag than Gerald. Jack gives 5 notebooks to Paula and 6 notebooks to Mike. If Gerald has 8 notebooks, how many notebooks does Jack have left?"""
    gerald_notebooks = 8
    jack_notebooks = gerald_notebooks + 13
    jack_notebooks -= 5  # Jack gives 5 notebooks to Paula
    jack_notebooks -= 6  # Jack gives 6 notebooks to Mike
    result = jack_notebooks
    return result

print(solution())