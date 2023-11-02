def solution():
    """Katie has 13 pink marbles. She has 9 fewer orange marbles than pink marbles. She has 4 times as many purple marbles as orange marbles. How many marbles does Katie have in all?"""
    # Define the number of pink marbles
    pink_marbles = 13

    # Calculate the number of orange marbles
    orange_marbles = pink_marbles - 9

    # Calculate the number of purple marbles
    purple_marbles = 4 * orange_marbles

    # Calculate the total number of marbles
    total_marbles = pink_marbles + orange_marbles + purple_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())