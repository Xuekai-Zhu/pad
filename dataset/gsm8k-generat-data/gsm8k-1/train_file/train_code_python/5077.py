def solution():
    """Megan bought 2 dozen eggs. As she was walking to her car, she dropped a tray of eggs. 3 eggs broke, and twice as many cracked. What is the difference between the eggs that are still in perfect condition and those that are cracked?"""
    dozen = 12
    total_eggs = 2 * dozen
    broken_eggs = 3
    cracked_eggs = 2 * broken_eggs
    perfect_eggs = total_eggs - broken_eggs - cracked_eggs
    cracked_difference = cracked_eggs - perfect_eggs
    result = cracked_difference
    return result

print(solution())