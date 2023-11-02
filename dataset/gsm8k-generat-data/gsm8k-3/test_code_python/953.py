def solution():
    """Wendi brought home 4 chickens.  After a few days, she brought home enough additional chickens to double the number of chickens she owned.  Then, a neighbor's dog ate one of her chickens.  Finally, Wendi found an additional 4 less than ten chickens and brought them home too.  After this, how many chickens does Wendi have?"""
    # Define the initial number of chickens
    initial_chickens = 4

    # Double the number of chickens
    doubled_chickens = initial_chickens * 2

    # Subtract the chicken eaten by the dog
    remaining_chickens = doubled_chickens - 1

    # Find the additional chickens Wendi found
    additional_chickens = 10 - 4

    # Add the additional chickens to remaining chickens
    total_chickens = remaining_chickens + additional_chickens

    # Display the total number of chickens Wendi has
    result = total_chickens
    return result

print(solution())