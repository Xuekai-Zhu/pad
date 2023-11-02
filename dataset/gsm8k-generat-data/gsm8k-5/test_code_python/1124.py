def solution():
    # Calculate how many of each type of clothing is in the hamper
    blouses_in_hamper = 0.75 * 12
    skirts_in_hamper = 0.5 * 6
    slacks_in_hamper = 0.25 * 8

    # Calculate the total number of pieces of clothing in the hamper
    total_in_hamper = blouses_in_hamper + skirts_in_hamper + slacks_in_hamper
    result = total_in_hamper
    return result

print(solution())