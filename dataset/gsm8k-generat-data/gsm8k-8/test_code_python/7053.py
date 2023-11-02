def solution():
    # Define the number of red and blue marbles initially
    red_marbles = 20
    blue_marbles = 30

    # Remove 3 red marbles and 4 times as many blue marbles as red marbles
    red_marbles -= 3
    blue_marbles -= 4 * 3

    # Calculate the total number of marbles remaining
    total_marbles = red_marbles + blue_marbles
    result = total_marbles
    return result

print(solution())