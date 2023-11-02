def solution():
    """Megan bought 2 dozen eggs. As she was walking to her car, she dropped a tray of eggs. 3 eggs broke, and twice as many cracked. What is the difference between the eggs that are still in perfect condition and those that are cracked?"""
    # Define the number of eggs in a dozen
    EGGS_PER_DOZEN = 12

    # Define the initial number of eggs Megan had
    initial_eggs = 2 * EGGS_PER_DOZEN

    # Calculate the number of eggs that are broken and cracked
    broken_eggs = 3
    cracked_eggs = 2 * broken_eggs

    # Calculate the number of eggs that are still in perfect condition and those that are cracked
    perfect_eggs = initial_eggs - broken_eggs - cracked_eggs
    cracked_difference = perfect_eggs - cracked_eggs

    # Display the difference between the perfect and cracked eggs
    result = cracked_difference
    return result

print(solution())