def solution():
    """Three times the sum of marbles that Atticus, Jensen, and Cruz have is equal to 60. If Atticus has half as many marbles as Jensen, and Atticus has 4 marbles, how many marbles does Cruz have?"""
    # Define the number of marbles Atticus has
    atticus_marbles = 4

    # Define the ratio of Jensen's marbles to Atticus's marbles
    jensen_atticus_ratio = 2

    # Calculate the number of marbles Jensen has
    jensen_marbles = atticus_marbles * jensen_atticus_ratio

    # Calculate the sum of marbles Atticus, Jensen, and Cruz have
    total_marbles = (atticus_marbles + jensen_marbles + cruz_marbles)
    # 3 times the sum of marbles is equal to 60
    # 3 * total_marbles = 60
    # total_marbles = 20

    # Calculate the number of marbles Cruz has
    cruz_marbles = 20 - atticus_marbles - jensen_marbles

    # Display the number of marbles Cruz has
    result = cruz_marbles
    return result

print(solution())