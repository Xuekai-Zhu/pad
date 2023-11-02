def solution():
    """A jar full of marbles is sitting on a table. Half of the marbles are blue, a quarter of them are red, 27 of them are green, and 14 of them are yellow. How many marbles are in the jar?"""
    # Define the fractions of marbles
    blue_fraction = 0.5
    red_fraction = 0.25

    # Calculate the total number of green and yellow marbles
    green_yellow_total = 27 + 14

    # Calculate the total fraction of blue and red marbles
    blue_red_total_fraction = 1 - (green_yellow_total / (1 - blue_fraction - red_fraction))

    # Calculate the total number of marbles
    total_marbles = green_yellow_total / (blue_red_total_fraction + red_fraction + blue_fraction)

    # Round the result to the nearest whole number
    result = round(total_marbles)
    return result

print(solution())