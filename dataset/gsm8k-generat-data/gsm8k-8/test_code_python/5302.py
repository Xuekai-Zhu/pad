def solution():
    # Calculate the total number of eggs
    total_eggs = 3 * 12

    # Calculate the total number of omelets that can be made
    total_omelets = total_eggs // 4

    # Calculate the number of omelets per person
    omelets_per_person = total_omelets // 3

    result = omelets_per_person
    return result

print(solution())