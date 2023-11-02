def solution():
    # Calculate the number of ducks and chickens
    ducks = 15/3
    chickens = 15 - ducks

    # Calculate the cost to feed the chickens
    chicken_feed_cost = chickens * 2

    result = chicken_feed_cost
    return result

print(solution())