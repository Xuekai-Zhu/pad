def solution():
    chicken_price = 1.5
    feed_price = 2
    feed_weight_per_chicken = 2
    total_profit = 65

    # Calculate the cost of feed per chicken
    feed_cost_per_chicken = (feed_price / 20) * feed_weight_per_chicken

    # Calculate the profit per chicken
    profit_per_chicken = chicken_price - feed_cost_per_chicken

    # Calculate the number of chickens sold to make the total profit
    num_chickens_sold = total_profit / profit_per_chicken
    result = num_chickens_sold
    return result

print(solution())