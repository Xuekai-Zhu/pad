def solution():
    """A papaya tree will grow 2 feet in the first year. In the second year, it will grow 50% more than the first year. In the third year, the tree will grow 50% more than in the second year. In the fourth year, it will grow twice as much as the third year. In the fifth year, it will grow half as much as the fourth year. When the tree is 5 years old, how tall is the tree?"""
    # Define the initial height of the tree
    height = 2

    # Calculate the height of the tree in the second year
    height *= 1.5

    # Calculate the height of the tree in the third year
    height *= 1.5

    # Calculate the height of the tree in the fourth year
    height *= 2

    # Calculate the height of the tree in the fifth year
    height *= 0.5

    # return the height of the tree at 5 years old
    result = height
    return result

print(solution())