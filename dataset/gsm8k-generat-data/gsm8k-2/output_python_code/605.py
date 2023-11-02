def solution():
    """In a big box, there are marbles in 4 colors. Inside, there are 20 red marbles. There are three times more green marbles than red. Yellow marbles make up 20% of the green marbles. How many marbles are of a different color if the total of all marbles in the box is three times more than the number of green marbles?"""
    red_marbles = 20
    green_marbles = 3 * red_marbles
    yellow_marbles = 0.2 * green_marbles
    total_marbles = 3 * green_marbles
    blue_marbles = total_marbles - (red_marbles + green_marbles + yellow_marbles)
    result = blue_marbles
    return result

print(solution())