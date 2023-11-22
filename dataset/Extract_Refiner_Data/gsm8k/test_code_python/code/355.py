def solution():
    
    # Define the initial amount of money Billy has
    initial_money = 10

    # Define the cost of the candy and the cost of gumballs
    candy_cost = 1.5
    gumball_cost = 0.05

    # Calculate the amount of money Billy has left after buying candy
    money_left = initial_money - candy_cost

    # Calculate the cost of the gumballs
    gumballs_cost = 40 * gumball_cost

    # Calculate the amount of money Billy spends on candy
    candy_cost_after_candy = money_left / 2

    # Calculate the total cost of the candy
    total_cost = candy_cost_after_candy + gumballs_cost

    # Return the result
    result = total_cost
    return result

print(solution())