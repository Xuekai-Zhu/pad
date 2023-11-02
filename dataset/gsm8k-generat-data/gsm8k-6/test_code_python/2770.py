def solution():
    # Calculate the total cost of Robert's order
    robert_pizza_cost = 5 * 10
    robert_drinks_cost = 10 * 2
    robert_total_cost = robert_pizza_cost + robert_drinks_cost

    # Calculate the total cost of Teddy's order
    teddy_hamburgers_cost = 6 * 3
    teddy_drinks_cost = 10 * 2
    teddy_total_cost = teddy_hamburgers_cost + teddy_drinks_cost

    # Calculate the total cost of snacks for their friends
    total_cost = robert_total_cost + teddy_total_cost
    result = total_cost
    return result

print(solution())