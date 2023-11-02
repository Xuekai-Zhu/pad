def solution():
    starting_money = 40
    pizza_cost = 2.75
    soda_cost = 1.5
    jeans_cost = 11.5

    # Calculate the total cost of all items
    total_cost = pizza_cost + soda_cost + jeans_cost

    # Calculate the amount of money Phil has left after buying all items
    remaining_money = starting_money - total_cost

    # Calculate the number of quarters Phil has left
    num_quarters = remaining_money / 0.25
    result = num_quarters
    return result

print(solution())