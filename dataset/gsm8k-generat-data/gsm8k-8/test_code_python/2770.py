def solution():
    # Calculate Robert's total cost
    robert_pizza_cost = 5 * 10
    robert_drink_cost = 10 * 2
    robert_total_cost = robert_pizza_cost + robert_drink_cost

    # Calculate Teddy's total cost
    teddy_hamburger_cost = 6 * 3
    teddy_drink_cost = 10 * 2
    teddy_total_cost = teddy_hamburger_cost + teddy_drink_cost

    # Calculate the total cost for both of them
    total_cost = robert_total_cost + teddy_total_cost
    result = total_cost
    return result

print(solution())