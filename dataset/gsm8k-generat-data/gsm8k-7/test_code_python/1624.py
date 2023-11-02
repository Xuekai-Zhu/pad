def solution():
    pork_price = 6
    chicken_price = pork_price - 2
    num_pork_kgs = 1
    num_chicken_kgs = 3

    # Calculate the total cost of pork
    pork_cost = num_pork_kgs * pork_price

    # Calculate the total cost of chicken
    chicken_cost = num_chicken_kgs * chicken_price

    # Calculate the total cost of one kilogram of pork and three kilograms of chicken
    total_cost = pork_cost + chicken_cost

    result = total_cost
    return result

print(solution())