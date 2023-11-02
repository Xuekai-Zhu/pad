def solution():
    initial_money = 20  # Todd has $20 initially
    cost_per_candy_bar = 2  # Each candy bar costs $2
    num_candy_bars_bought = 4  # Todd buys 4 candy bars

    # Calculate the total cost of the candy bars
    total_cost = cost_per_candy_bar * num_candy_bars_bought

    # Calculate the money left with Todd
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())