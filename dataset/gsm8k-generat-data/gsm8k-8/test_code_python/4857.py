def solution():
    # Calculate the total number of pigeon chicks
    total_pigeon_chicks = 40 * 6

    # Calculate the number of pigeons after the peregrines eat 30%
    pigeons_left = 40 - (40 * 0.3)

    # Calculate the total number of pigeon chicks left
    total_chicks_left = pigeons_left * 6

    result = total_chicks_left
    return result

print(solution())