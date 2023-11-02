def solution():
    num_gerald_notebooks = 8
    num_jack_notebooks = num_gerald_notebooks + 13

    # Jack gives 5 notebooks to Paula
    num_jack_notebooks -= 5

    # Jack gives 6 notebooks to Mike
    num_jack_notebooks -= 6

    result = num_jack_notebooks
    return result

print(solution())