def solution():
    num_cattle = 100
    cattle_cost = 40000

    # Calculate the cost of feeding the cattle
    feed_cost = cattle_cost * 1.20

    # Calculate the total weight of all cattle
    total_weight = num_cattle * 1000

    # Calculate the total revenue from selling all cattle
    total_revenue = total_weight * 2

    # Calculate the total profit
    total_profit = total_revenue - feed_cost - cattle_cost
    result = total_profit
    return result

print(solution())