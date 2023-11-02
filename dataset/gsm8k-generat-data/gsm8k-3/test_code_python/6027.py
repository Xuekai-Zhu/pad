def solution():
    """A family had 10 eggs, but the mother used 5 of them to make an omelet. Then, 2 chickens laid 3 eggs each. How many eggs does the family have now?"""
    # Calculate the number of eggs after the mother made the omelet
    eggs_after_omelet = 10 - 5

    # Calculate the number of eggs laid by the chickens
    eggs_laid = 2 * 3

    # Calculate the total number of eggs the family has now
    total_eggs = eggs_after_omelet + eggs_laid

    # Display the total number of eggs the family has now
    result = total_eggs
    return result

print(solution())