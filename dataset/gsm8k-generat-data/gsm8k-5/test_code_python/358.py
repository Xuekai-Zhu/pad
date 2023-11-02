def solution():
    # Calculate the number of marbles Carl had before the game
    initial_marbles = 2 * (12 / 0.5)  # Carl took out 12 marbles and lost 1/2 of them, so he had twice as many before

    # Calculate the total number of marbles after the game and the new bag
    total_marbles = initial_marbles + 10 + 25

    result = total_marbles
    return result

print(solution())