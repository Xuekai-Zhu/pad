def solution():
    """Jar A has 28 marbles. Jar B has 12 more marbles than jar A. Jar C has twice as many marbles as jar B. How many marbles are there altogether?"""
    # Define the number of marbles in each jar
    A = 28
    B = A + 12
    C = 2 * B

    # Calculate the total number of marbles
    total = A + B + C

    # Display the total number of marbles
    result = total
    return result

print(solution())