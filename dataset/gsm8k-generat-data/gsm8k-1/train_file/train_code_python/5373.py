def solution():
    """A jar full of marbles is sitting on a table. Half of the marbles are blue, a quarter of them are red, 27 of them are green, and 14 of them are yellow. How many marbles are in the jar?"""
    green_m = 27
    yellow_m = 14
    blue_m = red_m = 0.25 * (green_m + yellow_m)
    total_m = green_m + yellow_m + blue_m + red_m
    result = total_m * 2
    return result

print(solution())