def solution():
    # Calculate the total number of pigeon chicks
    pigeon_chicks = 40 * 6  # each pigeon has 6 chicks

    # Calculate the number of pigeons left after 30% are eaten by peregrines
    pigeons_left = int(40 - (40 * 0.3))  # 30% of 40 pigeons = 12 pigeons eaten, remaining pigeons = 28

    # Calculate the total number of chicks from the remaining pigeons
    chicks_left = pigeons_left * 6

    result = chicks_left
    return result

print(solution())