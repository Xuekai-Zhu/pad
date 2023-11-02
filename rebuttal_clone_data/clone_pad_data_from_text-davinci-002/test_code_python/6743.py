def solution():
    cost_per_head = 40000
    cost_of_feed = cost_per_head * 1.2
    cattle_weight = 1000
    price_per_pound = 2
    total_sale_price = cattle_weight * price_per_pound
    total_profit = total_sale_price - (cost_per_head + cost_of_feed)
    result = total_profit
    return result

print(solution())