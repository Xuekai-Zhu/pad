def solution():
    """Three times the sum of marbles that Atticus, Jensen, and Cruz have is equal to 60. If Atticus has half as many marbles as Jensen, and Atticus has 4 marbles, how many marbles does Cruz have?"""
    # Define the number of marbles Atticus has
    atticus_marbles = 4

    # Calculate the number of marbles Jensen has
    jensen_marbles = atticus_marbles * 2

    # Calculate the sum of marbles Atticus, Jensen, and Cruz have
    total_marbles = (atticus_marbles + jensen_marbles + cruz_marbles)

    # Calculate the number of marbles Cruz has
    cruz_marbles = (60 / 3 - total_marbles)

    # Return the result
    result = cruz_marbles
    return result

print(solution())