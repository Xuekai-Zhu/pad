def solution():
    """Addilynn went to the grocery store and bought six dozen eggs for use in her house. After two weeks, she used half of the eggs, then accidentally broke 15 of the remaining eggs while moving them to clean the shelves. How many eggs are left on the shelf?"""
    # Define the initial number of eggs
    initial_eggs = 6 * 12

    # Calculate the number of eggs used after two weeks
    used_eggs = initial_eggs / 2

    # Calculate the number of eggs remaining after two weeks
    remaining_eggs = initial_eggs - used_eggs

    # Subtract the eggs that were accidentally broken
    final_eggs = remaining_eggs - 15

    result = final_eggs
    return result

print(solution())