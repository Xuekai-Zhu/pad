def solution():
    # Calculate the total cost of the tuna packs
    tuna_cost = 5 * 2  # Barbara bought 5 packs of tuna for $2 each

    # Calculate the total cost of the water bottles
    water_cost = 4 * 1.5  # Barbara bought 4 bottles of water for $1.5 each

    # Calculate the total cost of the shopping
    total_cost = 56  # Barbara paid $56 in total

    # Calculate the cost of items other than tuna and water
    other_cost = total_cost - tuna_cost - water_cost
    result = other_cost
    return result

print(solution())