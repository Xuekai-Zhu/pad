def solution():
    """A jar full of marbles is sitting on a table. Half of the marbles are blue, a quarter of them are red, 27 of them are green, and 14 of them are yellow. How many marbles are in the jar?"""
    green_marbles = 27
    yellow_marbles = 14
    total_green_and_yellow_marbles = green_marbles + yellow_marbles
    red_marbles = 0.25 * (total_green_and_yellow_marbles)
    blue_marbles = 0.5 * (total_green_and_yellow_marbles)
    total_marbles = total_green_and_yellow_marbles + red_marbles + blue_marbles
    result = total_marbles
    return result

print(solution())