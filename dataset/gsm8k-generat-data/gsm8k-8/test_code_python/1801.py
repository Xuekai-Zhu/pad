def solution():
    # Define the initial number of eggs
    initial_eggs = 6 * 12

    # Calculate the number of eggs used after two weeks
    used_eggs = initial_eggs / 2

    # Calculate the number of eggs left after the accident
    remaining_eggs = initial_eggs - used_eggs - 15
    result = remaining_eggs
    return result

print(solution())