def solution():
    blue_marbles = 24 / 2  # Half of the marbles are blue
    red_marbles = 6  # There are 6 red marbles
    total_known_marbles = blue_marbles + red_marbles  # Total number of marbles we know the color of

    # Calculate the number of orange marbles
    orange_marbles = 24 - total_known_marbles
    result = orange_marbles
    return result

print(solution())