def solution():
    """On Sunday Alice bought 4 pints of strawberry ice cream. The next day she went back and bought three times that number of pints. On Tuesday she bought one-third of the number of pints she bought the day before. On Wednesday she returned half of the pints she bought the day before because they were expired. How many pints of ice cream did she have on Wednesday?"""
    # Define the initial number of pints of ice cream
    ice_cream = 4

    # Buy three times as many pints on Monday
    ice_cream += 3 * ice_cream

    # Buy one-third as many pints on Tuesday
    ice_cream += ice_cream / 3

    # Return half of the pints on Wednesday
    ice_cream /= 2

    # return the result
    result = ice_cream
    return result

print(solution())