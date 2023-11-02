def solution():
    first_debut_year = 1945
    monty_python_year = 1969
    if monty_python_year > first_debut_year:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())