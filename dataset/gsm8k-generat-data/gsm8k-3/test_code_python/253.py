def solution():
    """One pie costs $4 for a piece. Each pie is having 3 pieces. During one hour the bakery can make 12 pies. Creating one pie costs the bakery $0.5. Considering the bakery would be able to sell all pie pieces, how much money would it make?"""
    # Define the cost and selling price of a pie
    COST_PER_PIE = 0.5
    SELLING_PRICE_PER_PIECE = 4 / 3

    # Calculate the total cost of making 12 pies
    total_cost = COST_PER_PIE * 12

    # Calculate the total revenue from selling all the pie pieces
    total_revenue = SELLING_PRICE_PER_PIECE * 12 * 3

    # Calculate the profit made by the bakery
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())