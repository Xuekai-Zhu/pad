def solution():
    """Out of the 500 marbles that Cindy had, she gave her four friends 80 marbles each. What's four times the number of marbles she has remaining?"""
    starting_marbles = 500
    friends = 4
    marbles_given = friends * 80
    remaining_marbles = starting_marbles - marbles_given
    result = 4 * remaining_marbles
    return result

print(solution())