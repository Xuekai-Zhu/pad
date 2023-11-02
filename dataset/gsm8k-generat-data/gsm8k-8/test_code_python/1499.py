def solution():
    # Calculate the total earned from the family
    family_cost = 4 * 5 + 3 * 2

    # Calculate the total earned from the rest of the customers
    rest_of_customers_cost = 10 * 2 * 2

    # Calculate the total earned during the lunch rush
    total_cost = family_cost + rest_of_customers_cost
    result = total_cost
    return result

print(solution())