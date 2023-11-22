def solution():
    
    # Define the cost and selling price of each egg
    COST_PER_DOZEN = 2.4
    SELLING_PRICE_PER_EGG = 1

    # Define the number of dozens of eggs purchased
    dozens_purchased = 5

    # Calculate the total cost of the eggs purchased
    total_cost = dozens_purchased * COST_PER_DOZEN

    # Calculate the total revenue from selling the eggs
    total_revenue = 3 * SELLING_PRICE_PER_EGG

    # Calculate Rose's profit
    profit = total_revenue - total_cost

    # Display Rose's profit
    result = profit
    return result

print(solution())