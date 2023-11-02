def solution():
    """There were 10000 spectators at a basketball match. 7000 of them were men. Of the remaining spectators, there were 5 times as many children as women. How many children were there?"""
    # Define the number of men
    men = 7000

    # Calculate the number of women
    women = 10000 - men

    # Calculate the number of remaining spectators
    remaining = women

    # Calculate the number of children
    children = 5 * remaining

    # Display the number of children
    result = children
    return result

print(solution())