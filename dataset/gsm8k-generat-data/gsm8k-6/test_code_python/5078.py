def solution():
    # Calculate the total number of eggs Megan bought
    eggs_bought = 2 * 12  # 2 dozens of eggs

    # Calculate the total number of broken and cracked eggs
    broken_eggs = 3
    cracked_eggs = 2 * 3  # twice the number of broken eggs
    damaged_eggs = broken_eggs + cracked_eggs

    # Calculate the number of perfect eggs remaining
    perfect_eggs = eggs_bought - damaged_eggs

    # Calculate the difference between perfect eggs and cracked eggs
    difference = perfect_eggs - cracked_eggs

    result = difference
    return result

print(solution())