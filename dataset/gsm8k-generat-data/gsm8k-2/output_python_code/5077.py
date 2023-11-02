def solution():
    """Megan bought 2 dozen eggs. As she was walking to her car, she dropped a tray of eggs. 3 eggs broke, and twice as many cracked. What is the difference between the eggs that are still in perfect condition and those that are cracked?"""
    total_eggs = 2 * 12
    broken_eggs = 3
    cracked_eggs = 2 * 3
    perfect_eggs = total_eggs - broken_eggs - cracked_eggs
    difference = perfect_eggs - cracked_eggs
    result = difference
    return result

print(solution())