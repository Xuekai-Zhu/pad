def solution():
    """Jen buys and sells candy bars. She buys candy bars for 80 cents each and sells them for a dollar each. If she buys 50 candy bars and sells 48 of them, how much profit does she make in cents?"""
    # Define the cost and selling price of each candy bar
    COST_PER_BAR = 80
    SELLING_PRICE_PER_BAR = 100

    # Define the number of candy bars purchased and sold
    num_purchased = 50
    num_sold = 48

    # Calculate the total cost of the candy bars
    total_cost = num_purchased * COST_PER_BAR

    # Calculate the total revenue from selling the candy bars
    total_revenue = num_sold * SELLING_PRICE_PER_BAR

    # Calculate the profit in cents
    profit = (total_revenue - total_cost)

    # Display the profit in cents
    result = profit
    return result

print(solution())