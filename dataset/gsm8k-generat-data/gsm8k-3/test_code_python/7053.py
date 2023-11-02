def solution():
    """A magician has a top hat with 20 red marbles and a top hat with 30 blue marbles. If he takes away 3 red marbles and four times as many blue marbles as red marbles (without looking), how many marbles in total does he have left?"""
    # Define the initial number of red and blue marbles
    red_marbles = 20
    blue_marbles = 30

    # Take away 3 red marbles and 4 times as many blue marbles as red marbles
    red_marbles -= 3
    blue_marbles -= 4 * 3

    # Calculate the total number of marbles left
    total_marbles = red_marbles + blue_marbles

    # Display the total number of marbles left
    result = total_marbles
    return result

print(solution())