def solution():
    num_ducks = 15 / 3  # Number of ducks is 1/3 of the total birds
    num_chickens = 15 - num_ducks  # Remaining birds are chickens
    cost_per_chicken = 2  # Special feed for chickens costs $2 per bird

    # Calculate the total cost to feed the chickens
    total_cost = num_chickens * cost_per_chicken
    result = total_cost
    return result

print(solution())