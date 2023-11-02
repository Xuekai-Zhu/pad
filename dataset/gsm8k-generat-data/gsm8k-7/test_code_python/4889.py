def solution():
    total_birds = 15
    ducks = total_birds / 3
    chickens = total_birds - ducks
    cost_per_chicken = 2.0

    # Calculate the total cost to feed the chickens
    total_cost = chickens * cost_per_chicken
    result = total_cost
    return result

print(solution())