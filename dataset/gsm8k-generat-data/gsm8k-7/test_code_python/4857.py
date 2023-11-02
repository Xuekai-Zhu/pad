def solution():
    num_peregrines = 6
    num_pigeons = 40
    num_chicks_per_pigeon = 6
    percent_pigeons_eaten = 0.3

    # Calculate the total number of pigeon chicks
    total_pigeon_chicks = num_pigeons * num_chicks_per_pigeon

    # Calculate the number of pigeons eaten by the peregrines
    num_pigeons_eaten = num_pigeons * percent_pigeons_eaten

    # Calculate the total number of remaining pigeons
    total_pigeons_remaining = num_pigeons - num_pigeons_eaten

    result = total_pigeons_remaining
    return result

print(solution())