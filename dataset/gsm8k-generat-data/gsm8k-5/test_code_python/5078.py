def solution():
    eggs_per_dozen = 12  # There are 12 eggs in a dozen
    total_eggs = 2 * eggs_per_dozen  # Megan bought 2 dozen eggs

    # Calculate the number of eggs that are still in perfect condition
    perfect_eggs = total_eggs - 3 - (2 * 3)  # 3 eggs broke and twice as many cracked

    # Calculate the number of eggs that are cracked
    cracked_eggs = 2 * 3  # Twice as many eggs cracked as broke

    # Calculate the difference between the perfect eggs and cracked eggs
    difference = perfect_eggs - cracked_eggs
    result = difference
    return result

print(solution())