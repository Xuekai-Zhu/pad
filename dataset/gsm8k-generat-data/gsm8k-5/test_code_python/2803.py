def solution():
    cost_per_candy_bar = 2  # Each candy bar costs $2
    num_candy_bars = 4  # Todd buys 4 candy bars
    total_cost = cost_per_candy_bar * num_candy_bars  # Calculate the total cost of the candy bars

    # Calculate how much money Todd has left after buying the candy bars
    money_left = 20 - total_cost
    result = money_left
    return result

print(solution())