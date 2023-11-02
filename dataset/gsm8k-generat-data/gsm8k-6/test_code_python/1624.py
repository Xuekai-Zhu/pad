def solution():
    # Calculate the cost of 1 kilogram of chicken
    chicken_cost = 6 - 2  # a kilogram of chicken costs $2 less

    # Calculate the total cost of 3 kilograms of chicken and 1 kilogram of pork
    total_cost = (3 * chicken_cost) + 6

    result = total_cost
    return result

print(solution())