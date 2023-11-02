def solution():
    """A magician has a top hat with 20 red marbles and a top hat with 30 blue marbles. If he takes away 3 red marbles and four times as many blue marbles as red marbles (without looking), how many marbles in total does he have left?"""
    # Define the number of red and blue marbles in the top hats
    red_marbles = 20
    blue_marbles = 30

    # Take away 3 red marbles
    red_marbles -= 3

    # Take away 4 times as many blue marbles as red marbles
    blue_marbles -= 4 * 3

    # Calculate the total number of marbles remaining
    total_marbles = red_marbles + blue_marbles

    result = total_marbles
    return result

print(solution())