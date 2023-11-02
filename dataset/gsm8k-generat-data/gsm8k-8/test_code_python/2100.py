def solution():
    # Calculate the total cost of the pizzas
    pizza_cost = 2 * 12

    # Calculate the total cost of the juice drinks
    juice_cost = 2 * 2

    # Calculate the total cost of the snacks
    total_cost = pizza_cost + juice_cost

    # Calculate the amount to be returned to Victoria's mother
    return_amount = 50 - total_cost
    result = return_amount
    return result

print(solution())