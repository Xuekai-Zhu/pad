def solution():
    """Camille saw 3 cardinals and four times as many robins as cardinals while bird watching. She also saw twice as many blue jays as cardinals and 1 more than three times as many sparrows as cardinals. How many birds did Camille see?"""
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

    # Display the total number of birds
    result = total_birds
    return result

print(solution())