def solution():
    marbles_A = 28  # Jar A has 28 marbles
    marbles_B = marbles_A + 12  # Jar B has 12 more marbles than jar A
    marbles_C = 2 * marbles_B  # Jar C has twice as many marbles as jar B

    # Calculate the total number of marbles
    total_marbles = marbles_A + marbles_B + marbles_C
    result = total_marbles
    return result

print(solution())