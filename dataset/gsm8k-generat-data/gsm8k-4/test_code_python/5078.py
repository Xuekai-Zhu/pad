def solution():
    """Megan bought 2 dozen eggs. As she was walking to her car, she dropped a tray of eggs. 3 eggs broke, and twice as many cracked. What is the difference between the eggs that are still in perfect condition and those that are cracked?"""
    
    # Define the total number of eggs
    total_eggs = 2 * 12

    # Calculate the number of eggs that broke
    broke_eggs = 3

    # Calculate the number of eggs that cracked
    cracked_eggs = 2 * broke_eggs

    # Calculate the number of perfect eggs
    perfect_eggs = total_eggs - broke_eggs - cracked_eggs

    # Calculate the difference between perfect eggs and cracked eggs
    difference = perfect_eggs - cracked_eggs

    # Return the result
    result = difference
    return result

print(solution())