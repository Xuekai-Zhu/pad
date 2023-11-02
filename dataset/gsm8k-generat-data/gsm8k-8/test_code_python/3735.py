def solution():
    # Define the number of cardinals
    cardinals = 3

    # Calculate the number of robins
    robins = 4 * cardinals

    # Calculate the number of blue jays
    blue_jays = 2 * cardinals

    # Calculate the number of sparrows
    sparrows = 3 * cardinals + 1

    # Calculate the total number of birds
    total_birds = cardinals + robins + blue_jays + sparrows
    result = total_birds
    return result

print(solution())