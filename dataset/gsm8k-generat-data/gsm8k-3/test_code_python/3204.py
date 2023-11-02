def solution():
    """Mark has two dozen eggs to split with his three siblings. How many eggs does each person get to eat if they all eat the same amount?"""
    # Define the number of eggs and the number of siblings
    eggs = 24
    siblings = 3

    # Divide the number of eggs evenly among the siblings
    eggs_per_sibling = eggs / siblings

    # Display the number of eggs each sibling gets to eat
    result = eggs_per_sibling
    return result

print(solution())