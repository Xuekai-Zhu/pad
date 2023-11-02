def solution():
    """Adam has 18 magnets. He gave away a third of the magnets, and he still had half as many magnets as Peter. How many magnets does Peter have?"""
    # Define the initial number of magnets Adam has
    adam_magnets = 18

    # Calculate the number of magnets Adam gave away
    given_magnets = adam_magnets // 3

    # Calculate the number of magnets Adam has left
    adam_magnets_left = adam_magnets - given_magnets

    # Calculate the number of magnets Peter has
    peter_magnets = adam_magnets_left * 2

    result = peter_magnets
    return result

print(solution())