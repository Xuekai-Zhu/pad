def solution():
    n_checkered = 7
    n_horizontal = n_checkered * 4
    n_vertical = 40 - n_checkered - n_horizontal
    result = n_vertical
    return result

print(solution())