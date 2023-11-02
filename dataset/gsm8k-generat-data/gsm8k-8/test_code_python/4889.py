def solution():
    # Calculate the number of ducks
    num_ducks = 15/3

    # Calculate the number of chickens
    num_chickens = 15 - num_ducks

    # Calculate the cost to feed the chickens
    chicken_cost = num_chickens * 2
    result = chicken_cost
    return result

print(solution())