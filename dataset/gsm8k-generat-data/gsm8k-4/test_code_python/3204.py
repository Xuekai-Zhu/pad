def solution():
    """Mark has two dozen eggs to split with his three siblings. How many eggs does each person get to eat if they all eat the same amount?"""
    # Define the number of eggs
    eggs = 2 * 12

    # Define the number of people
    people = 4

    # Calculate the number of eggs per person
    eggs_per_person = eggs / people

    # Return the result
    result = eggs_per_person
    return result

print(solution())