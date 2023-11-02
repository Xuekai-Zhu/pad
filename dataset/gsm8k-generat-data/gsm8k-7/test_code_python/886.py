def solution():
    initial_money = 100
    water_bottles = 4
    water_bottle_price = 2
    additional_bottles = 2 * water_bottles  # twice as many bottles as he already bought
    cheese_price_per_pound = 10
    cheese_weight = 0.5  # half a pound

    # Calculate the total cost of all water bottles
    total_water_cost = (water_bottles + additional_bottles) * water_bottle_price

    # Calculate the cost of the cheese
    cheese_cost = cheese_price_per_pound * cheese_weight

    # Calculate the total cost of all items
    total_cost = total_water_cost + cheese_cost

    # Calculate the remaining money
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())