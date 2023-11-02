def solution():
    """Elizabeth uses $3.00 worth of ingredients to make a  bag of granola.  She makes 20 bags and sells them for $6.00 a bag at the farmer's market.  An hour before closing, she has sold 15 bags and marks the remaining 5 bags down to $4.00 and sells them soon after.  What is her net profit?"""
    # Define the cost of ingredients and selling price
    INGREDIENT_COST = 3.00
    SELLING_PRICE = 6.00

    # Calculate the total revenue from selling all 20 bags at full price
    full_price_revenue = 20 * SELLING_PRICE

    # Calculate the revenue from selling the first 15 bags at full price
    partial_sales_revenue = 15 * SELLING_PRICE

    # Calculate the revenue from selling the last 5 bags at the discounted price
    discounted_sales_revenue = 5 * 4.00

    # Calculate the total cost of making all 20 bags
    total_cost = 20 * INGREDIENT_COST

    # Calculate the total profit from selling all 20 bags
    total_profit = full_price_revenue + discounted_sales_revenue - total_cost

    # Display the net profit
    result = total_profit
    return result

print(solution())