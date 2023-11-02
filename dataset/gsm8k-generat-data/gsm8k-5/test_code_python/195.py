def solution():
    # Calculate total cost of drinks
    drinks_cost = 5 * 6

    # Calculate total cost of pizzas
    pizza_cost = 10 * 14

    # Calculate total cost of all items
    total_cost = drinks_cost + pizza_cost

    # Calculate the change Mary received
    change = 200 - total_cost
    result = change
    return result

print(solution())