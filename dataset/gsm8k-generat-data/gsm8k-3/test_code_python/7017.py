def solution():
    """Mrs. Oaklyn buys handmade rugs at $40 each and sells them at $60 each. If she bought 20 rugs, calculate the profit she will make from selling the rugs."""
    # Define the cost and selling price of each rug
    COST_PER_RUG = 40
    SELLING_PRICE_PER_RUG = 60

    # Define the number of rugs purchased
    rugs_purchased = 20

    # Calculate the total cost of the rugs
    total_cost = rugs_purchased * COST_PER_RUG

    # Calculate the total revenue from selling the rugs
    total_revenue = rugs_purchased * SELLING_PRICE_PER_RUG

    # Calculate the profit from selling the rugs
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())