def solution():
    cattle_cost = 40000  # James bought 100 cows for $40,000
    feed_cost = 1.2 * cattle_cost  # It cost 20% more to feed the cattle than to buy them
    total_cost = cattle_cost + feed_cost  # Total cost includes cattle cost and feed cost
    cow_weight = 1000  # Each cow weighs 1000 pounds
    price_per_pound = 2  # Cows sell for $2 per pound
    total_weight = 100 * cow_weight  # Total weight of 100 cows
    total_sales = total_weight * price_per_pound  # Total sales from selling the cows

    # Calculate the profit made by James
    profit = total_sales - total_cost
    result = profit
    return result

print(solution())