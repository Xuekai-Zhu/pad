def solution():
    num_buns = 10
    bun_price = 0.1

    num_milk_bottles = 2
    milk_price = 2.0

    egg_price = 3 * milk_price

    # Calculate the total cost of all buns
    total_bun_cost = num_buns * bun_price

    # Calculate the total cost of all milk bottles
    total_milk_cost = num_milk_bottles * milk_price

    # Calculate the cost of the carton of eggs
    egg_cost = egg_price

    # Calculate the total cost of all items
    total_cost = total_bun_cost + total_milk_cost + egg_cost
    result = total_cost
    return result

print(solution())