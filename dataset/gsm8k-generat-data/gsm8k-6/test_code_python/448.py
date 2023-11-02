def solution():
    # Calculate the total number of marbles in all jars
    A = 28
    B = A + 12  # Jar B has 12 more marbles than Jar A
    C = 2 * B  # Jar C has twice as many marbles as Jar B
    total_marbles = A + B + C
    result = total_marbles
    return result

print(solution())