def solution():
    num_sandwiches = 3
    num_drinks = 2
    drink_price = 4
    total_cost = 26

    # Calculate the total cost of all drinks
    total_drink_cost = num_drinks * drink_price

    # Calculate the total cost of all sandwiches
    total_sandwich_cost = total_cost - total_drink_cost

    # Calculate the cost of each sandwich
    sandwich_cost = total_sandwich_cost / num_sandwiches
    result = sandwich_cost
    return result

print(solution())