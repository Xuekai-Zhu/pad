def solution():
    num_eggs = 20
    egg_price = 2.0

    num_chickens = 6
    chicken_price = 8.0

    # Calculate the total cost of all eggs
    total_eggs_cost = num_eggs * egg_price

    # Calculate the total cost of all chickens
    total_chickens_cost = num_chickens * chicken_price

    # Calculate the total cost of all items Alan bought
    total_cost = total_eggs_cost + total_chickens_cost
    result = total_cost
    return result

print(solution())