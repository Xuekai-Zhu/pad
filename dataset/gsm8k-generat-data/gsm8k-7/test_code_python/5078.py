def solution():
    num_eggs = 2 * 12
    num_broken_eggs = 3
    num_cracked_eggs = 2 * num_broken_eggs

    # Calculate the number of eggs that are still in perfect condition
    num_perfect_eggs = num_eggs - num_broken_eggs - num_cracked_eggs

    # Calculate the difference between the perfect eggs and the cracked eggs
    difference = num_perfect_eggs - num_cracked_eggs
    result = difference
    return result

print(solution())