def solution():
    """Out of the 500 marbles that Cindy had, she gave her four friends 80 marbles each. What's four times the number of marbles she has remaining?"""
    # Define the initial number of marbles
    initial_marbles = 500

    # Define the number of friends
    friends = 4

    # Calculate the total number of marbles given away
    marbles_given = friends * 80

    # Calculate the number of marbles remaining
    marbles_remaining = initial_marbles - marbles_given

    # Calculate four times the number of marbles remaining
    result = marbles_remaining * 4
    return result

print(solution())