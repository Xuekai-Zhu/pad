def solution():
    """Jar A has 28 marbles. Jar B has 12 more marbles than jar A. Jar C has twice as many marbles as jar B. How many marbles are there altogether?"""
    # Define the number of marbles in jar A
    jar_A = 28

    # Define the number of marbles in jar B (12 more than jar A)
    jar_B = jar_A + 12

    # Define the number of marbles in jar C (twice as many as jar B)
    jar_C = jar_B * 2

    # Calculate the total number of marbles
    total_marbles = jar_A + jar_B + jar_C

    # return the result
    result = total_marbles
    return result

print(solution())