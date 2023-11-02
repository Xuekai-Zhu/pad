def solution():
    """Mrs. Jackson has four boxes of Christmas decorations. There are 15 decorations in each box. She was only able to use 35 decorations and decided to give the rest to her neighbor. How many decorations did she give?"""
    # Define the number of decorations per box
    DECORATIONS_PER_BOX = 15

    # Define the total number of decorations Mrs. Jackson has
    total_decorations = DECORATIONS_PER_BOX * 4

    # Calculate the number of decorations Mrs. Jackson did not use
    unused_decorations = total_decorations - 35

    # Calculate the number of decorations Mrs. Jackson gave to her neighbor
    neighbor_decorations = unused_decorations

    # Display the number of decorations Mrs. Jackson gave to her neighbor
    result = neighbor_decorations
    return result

print(solution())