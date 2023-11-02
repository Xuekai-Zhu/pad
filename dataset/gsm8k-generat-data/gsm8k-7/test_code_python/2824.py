def solution():
    beef_weight = 100
    beef_per_taco = 0.25
    taco_sell_price = 2
    taco_cost_price = 1.5

    # Calculate the total number of tacos they can make
    num_tacos = beef_weight / beef_per_taco

    # Calculate the total revenue from selling all the tacos
    total_revenue = num_tacos * taco_sell_price

    # Calculate the total cost of making all the tacos
    total_cost = num_tacos * taco_cost_price

    # Calculate the profit from selling all the tacos
    total_profit = total_revenue - total_cost
    result = total_profit
    return result

print(solution())