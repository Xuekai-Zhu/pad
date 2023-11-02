def solution():
    """Henry went to the beach and picked up 17 perfect shells and 52 broken shells. Out of those 52 broken shells, half of them were spiral. Out of the 17 perfect shells, 12 of them were not spiral. How many more broken spiral shells were there than perfect spiral shells?"""
    # Define the number of perfect and broken shells
    perfect_shells = 17
    broken_shells = 52

    # Calculate the number of broken spiral shells and perfect spiral shells
    broken_spiral = broken_shells * 0.5
    perfect_spiral = (perfect_shells - 12) * 0.5

    # Calculate the difference between the broken and perfect spiral shells
    difference = broken_spiral - perfect_spiral

    # return the result
    result = difference
    return result

print(solution())