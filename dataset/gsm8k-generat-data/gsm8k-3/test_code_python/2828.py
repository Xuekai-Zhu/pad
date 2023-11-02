def solution():
    """Adam has 18 magnets. He gave away a third of the magnets, and he still had half as many magnets as Peter. How many magnets does Peter have?"""
    # Define Adam's original number of magnets
    adam_magnets = 18

    # Calculate the number of magnets Adam gave away
    given_away = adam_magnets//3

    # Calculate Adam's remaining number of magnets
    remaining = adam_magnets - given_away

    # Calculate Peter's number of magnets, which is double Adam's remaining number
    peter_magnets = remaining * 2

    # Display Peter's number of magnets
    result = peter_magnets
    return result

print(solution())