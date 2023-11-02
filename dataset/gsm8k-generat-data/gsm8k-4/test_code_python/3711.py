def solution():
    """If Katherine has 4 apples and 3 times as many pears in her fridge, how many bananas does she have if she has a total of 21 pieces of fruit?"""
    # Define the number of apples and pears
    apples = 4
    pears = 3 * apples

    # Calculate the number of bananas
    bananas = 21 - (apples + pears)

    # return the result
    result = bananas
    return result

print(solution())