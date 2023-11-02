def solution():
    # Calculate the number of orange marbles
    orange_marbles = 13 - 9 

    # Calculate the number of purple marbles
    purple_marbles = 4 * orange_marbles 

    # Calculate the total number of marbles
    total_marbles = 13 + orange_marbles + purple_marbles
    result = total_marbles
    return result

print(solution())