def solution():
    num_steaks = 4.5
    steak_price = 15
    num_chicken_breasts = 1.5
    chicken_price = 8

    # Calculate the total cost of steaks
    steak_cost = num_steaks * steak_price

    # Calculate the total cost of chicken breasts
    chicken_cost = num_chicken_breasts * chicken_price

    # Calculate the total cost of all items
    total_cost = steak_cost + chicken_cost
    result = total_cost
    return result

print(solution())