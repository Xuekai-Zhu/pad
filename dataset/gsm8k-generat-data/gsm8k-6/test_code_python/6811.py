def solution():
    # Calculate the number of blue marbles
    blue_marbles = 24 / 2  # Half of the marbles are blue

    # Calculate the number of orange marbles
    orange_marbles = 24 - blue_marbles - 6  # Subtract blue and red marbles from the total

    result = orange_marbles
    return result

print(solution())