def solution():
    """A magician has a top hat with 20 red marbles and a top hat with 30 blue marbles. If he takes away 3 red marbles and four times as many blue marbles as red marbles (without looking), how many marbles in total does he have left?"""
    red_marbles = 20 - 3
    blue_marbles = 30 - 4 * (20 - 3)
    total_marbles = red_marbles + blue_marbles
    result = total_marbles
    return result

print(solution())