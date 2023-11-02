def solution():
    gerald_notebooks = 8  # Gerald has 8 notebooks
    jack_notebooks = gerald_notebooks + 13  # Jack has 13 more notebooks than Gerald

    # Jack gives away 5 notebooks to Paula and 6 notebooks to Mike
    jack_notebooks = jack_notebooks - 5 - 6

    result = jack_notebooks
    return result

print(solution())