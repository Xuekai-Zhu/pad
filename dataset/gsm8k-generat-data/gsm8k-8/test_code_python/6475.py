def solution():
    # Define the number of marbles Atticus has
    atticus_marbles = 4

    # Calculate the number of marbles Jensen has
    jensen_marbles = 2 * atticus_marbles

    # Calculate the sum of marbles that Atticus and Jensen have
    atticus_jensen_marbles = atticus_marbles + jensen_marbles

    # Calculate the number of marbles Cruz has
    cruz_marbles = (60 / 3 - atticus_jensen_marbles) / 3

    result = cruz_marbles
    return result

print(solution())