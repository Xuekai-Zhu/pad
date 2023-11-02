def solution():
    """John buys bags of popcorn for $4 and sells them for $8.  How much profit does he get by selling 30 bags?"""
    # Define the cost and selling price of each bag of popcorn
    COST_PER_BAG = 4
    PRICE_PER_BAG = 8

    # Define the number of bags of popcorn sold
    NUM_BAGS_SOLD = 30

    # Calculate the profit from selling the bags of popcorn
    total_cost = COST_PER_BAG * NUM_BAGS_SOLD
    total_revenue = PRICE_PER_BAG * NUM_BAGS_SOLD
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())