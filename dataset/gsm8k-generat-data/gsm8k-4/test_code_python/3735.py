def solution():
    """Camille saw 3 cardinals and four times as many robins as cardinals while bird watching.
    She also saw twice as many blue jays as cardinals and 1 more than three times as many sparrows as cardinals.
    How many birds did Camille see?"""
    # Define the number of cardinals
    cardinals = 3

    # Calculate the number of robins
    robins = cardinals * 4

    # Calculate the number of blue jays
    blue_jays = cardinals * 2

    # Calculate the number of sparrows
    sparrows = cardinals * 3 + 1

    # Calculate the total number of birds
    total_birds = cardinals + robins + blue_jays + sparrows

    # return the result
    result = total_birds
    return result

print(solution())