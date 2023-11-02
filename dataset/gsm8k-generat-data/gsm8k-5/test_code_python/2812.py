def solution():
    cost_per_magazine = 3  # The cost of each magazine is $3
    selling_price_per_magazine = 3.5  # Jewel sells each magazine for $3.50
    num_magazines = 10  # Jewel bought 10 magazines to sell

    # Calculate the total cost of buying the magazines
    total_cost = cost_per_magazine * num_magazines

    # Calculate the total revenue from selling the magazines
    total_revenue = selling_price_per_magazine * num_magazines

    # Calculate the profit from selling the magazines
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())