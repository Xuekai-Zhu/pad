def solution():
    # Calculate the total number of pigeon chicks
    pigeon_chicks = 40 * 6

    # Calculate the number of pigeons eaten by the peregrines
    eaten_pigeons = round(0.3 * 40)

    # Calculate the number of pigeons left
    remaining_pigeons = 40 - eaten_pigeons

    result = remaining_pigeons
    return result

print(solution())