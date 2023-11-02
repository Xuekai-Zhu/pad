def solution():
    """Jennifer bought twice as many candies as Emily and three times as many as Bob bought. If Emily bought 6 candies, how many candies did Bob buy?"""
    # Define the number of candies Emily bought
    emily_candies = 6

    # Calculate the number of candies Jennifer bought
    jennifer_candies = emily_candies * 2

    # Calculate the number of candies Bob bought
    bob_candies = jennifer_candies / 3

    result = bob_candies
    return result

print(solution())