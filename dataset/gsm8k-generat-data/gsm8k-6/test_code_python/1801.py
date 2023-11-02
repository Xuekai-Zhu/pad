def solution():
    # Calculate the total number of eggs
    total_eggs = 6 * 12  # six dozen eggs

    # Calculate the number of eggs used after two weeks
    used_eggs = total_eggs / 2  # half of the eggs

    # Calculate the number of eggs left after accidentally breaking 15
    remaining_eggs = total_eggs - used_eggs - 15  # eggs left minus the ones used and broken
    result = remaining_eggs
    return result

print(solution())