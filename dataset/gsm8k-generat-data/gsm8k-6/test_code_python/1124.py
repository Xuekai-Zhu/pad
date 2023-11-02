def solution():
    # Calculate the number of clothes that are currently in the hamper
    blouses_in_hamper = 0.75 * 12
    skirts_in_hamper = 0.5 * 6
    slacks_in_hamper = 0.25 * 8
    total_in_hamper = blouses_in_hamper + skirts_in_hamper + slacks_in_hamper

    # Calculate the number of clothes that need to be put in the washer
    total_clothes = 12 + 6 + 8
    clothes_to_wash = total_clothes - total_in_hamper
    result = clothes_to_wash
    return result

print(solution())