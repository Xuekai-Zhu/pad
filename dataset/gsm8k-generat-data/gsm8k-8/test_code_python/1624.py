def solution():
    # Calculate the cost of 1 kilogram of chicken
    chicken_cost = 6 - 2

    # Calculate the total cost of 3 kilograms of chicken
    chicken_total_cost = 3 * chicken_cost

    # Calculate the total cost of 1 kilogram of pork
    pork_total_cost = 1 * 6

    # Calculate the total cost of 3 kilograms of chicken and 1 kilogram of pork
    total_cost = chicken_total_cost + pork_total_cost

    result = total_cost
    return result

print(solution())