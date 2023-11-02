def solution():
    num_tuna_packs = 5
    tuna_price = 2

    num_water_bottles = 4
    water_price = 1.5

    total_paid = 56

    # Calculate the total cost of tuna
    total_tuna_cost = num_tuna_packs * tuna_price

    # Calculate the total cost of water bottles
    total_water_cost = num_water_bottles * water_price

    # Calculate the total cost of all items except tuna and water
    total_cost = total_paid - total_tuna_cost - total_water_cost
    result = total_cost
    return result

print(solution())