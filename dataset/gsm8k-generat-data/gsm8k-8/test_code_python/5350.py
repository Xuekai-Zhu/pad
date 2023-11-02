def solution():
    # Define the number of pink marbles
    pink_marbles = 13

    # Calculate the number of orange marbles
    orange_marbles = pink_marbles - 9

    # Calculate the number of purple marbles
    purple_marbles = 4 * orange_marbles

    # Calculate the total number of marbles
    total_marbles = pink_marbles + orange_marbles + purple_marbles
    result = total_marbles
    return result

print(solution())