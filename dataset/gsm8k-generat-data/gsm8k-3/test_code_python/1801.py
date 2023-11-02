def solution():
    """Addilynn went to the grocery store and bought six dozen eggs for use in her house. 
    After two weeks, she used half of the eggs, then accidentally broke 15 of the remaining eggs 
    while moving them to clean the shelves. How many eggs are left on the shelf?"""
    
    # Define the number of eggs per dozen
    EGGS_PER_DOZEN = 12
    
    # Define the initial number of eggs purchased
    initial_eggs = 6 * EGGS_PER_DOZEN
    
    # Calculate the number of eggs used in the first two weeks
    used_eggs = 0.5 * initial_eggs
    
    # Calculate the number of eggs remaining after two weeks
    remaining_eggs = initial_eggs - used_eggs
    
    # Calculate the number of eggs left after 15 were broken
    left_eggs = remaining_eggs - 15
    
    # Display the number of eggs left on the shelf
    result = left_eggs
    return result

print(solution())