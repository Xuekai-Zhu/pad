def solution():
    """Elizabeth uses $3.00 worth of ingredients to make a  bag of granola.  She makes 20 bags and sells them for $6.00 a bag at the farmer's market.  An hour before closing, she has sold 15 bags and marks the remaining 5 bags down to $4.00 and sells them soon after.  What is her net profit?"""
    # Define the cost and selling price per bag of granola
    cost_per_bag = 3.0
    selling_price_per_bag = 6.0

    # Calculate the total cost and total revenue of making and selling 20 bags of granola
    total_cost = cost_per_bag * 20
    total_revenue = (selling_price_per_bag * 15) + (4.0 * 5)

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # Return the net profit
    result = net_profit
    return result

print(solution())