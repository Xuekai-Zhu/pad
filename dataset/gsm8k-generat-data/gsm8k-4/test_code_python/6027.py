def solution():
    """A family had 10 eggs, but the mother used 5 of them to make an omelet. Then, 2 chickens laid 3 eggs each. How many eggs does the family have now?"""
    # Define the initial number of eggs
    initial_eggs = 10

    # Calculate the number of eggs left after making an omelet
    eggs_left = initial_eggs - 5

    # Calculate the number of eggs laid by the chickens
    eggs_laid = 2 * 3

    # Calculate the total number of eggs the family has now
    total_eggs = eggs_left + eggs_laid

    # return the result
    result = total_eggs
    return result

print(solution())