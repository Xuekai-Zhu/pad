def solution():
    abe_ants = 4
    beth_ants = abe_ants * 1.5
    cece_ants = abe_ants * 2
    duke_ants = abe_ants / 2

    # Calculate the total number of ants the four children find together
    total_ants = abe_ants + beth_ants + cece_ants + duke_ants
    result = total_ants
    return result

print(solution())