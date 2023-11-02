def solution():
    # Calculate the total cost of the tuna packs
    tuna_cost = 5 * 2  # 5 packs of tuna for $2 each

    # Calculate the total cost of the water bottles
    water_cost = 4 * 1.5  # 4 bottles of water for $1.5 each

    # Calculate the total amount spent by Barbara
    total_cost = 56

    # Calculate the amount spent on items other than tuna and water
    other_cost = total_cost - tuna_cost - water_cost
    result = other_cost
    return result

print(solution())