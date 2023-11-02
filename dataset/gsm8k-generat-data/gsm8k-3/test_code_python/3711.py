def solution():
    """If Katherine has 4 apples and 3 times as many pears in her fridge, how many bananas does she have if she has a total of 21 pieces of fruit?"""
    # Number of apples Katherine has
    apples = 4

    # Number of pears Katherine has
    pears = apples * 3

    # Number of bananas Katherine has
    bananas = 21 - (apples + pears)

    # Display the number of bananas Katherine has
    result = bananas
    return result

print(solution())