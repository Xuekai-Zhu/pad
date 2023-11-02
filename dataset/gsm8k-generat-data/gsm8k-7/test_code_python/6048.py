def solution():
    num_sandwiches = 3
    sandwich_price = 3

    num_fruit_drinks = 2
    fruit_drink_price = 2.5

    # Calculate the total cost of all sandwiches
    total_sandwich_cost = num_sandwiches * sandwich_price

    # Calculate the total cost of all fruit drinks
    total_fruit_drink_cost = num_fruit_drinks * fruit_drink_price

    # Calculate the total cost of all snacks
    total_cost = total_sandwich_cost + total_fruit_drink_cost
    result = total_cost
    return result

print(solution())