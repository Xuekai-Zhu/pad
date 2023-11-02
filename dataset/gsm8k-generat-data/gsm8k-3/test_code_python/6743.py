def solution():
    """Jame's buys 100 head of cattle for $40,000.  It cost 20% more than that to feed them.  They each weigh 1000 pounds and sell for $2 per pound.  How much profit did he make?"""
    # Calculate the cost to feed the cattle
    feed_cost = 40000 * 1.2

    # Calculate the total cost of purchasing and feeding the cattle
    total_cost = 40000 + feed_cost

    # Calculate the total weight of the cattle
    total_weight = 100 * 1000

    # Calculate the total revenue from selling the cattle
    total_revenue = total_weight * 2

    # Calculate the profit made from selling the cattle
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())