def solution():
    """Prudence was starting a cupcake business.  She figured that each cupcake cost $0.75 to make.  The first 2 dozen that she made burnt and she had to throw them out.  The next 2 came out perfectly and she ended up eating 5 cupcakes right away.  Later that day she made 2 more dozen cupcakes and decided to eat 4 more. If she sells the remaining cupcakes at $2.00 each, how much is her net profit?"""
    # Define the cost and selling price of each cupcake
    COST_PER_CUPCAKE = 0.75
    SELLING_PRICE_PER_CUPCAKE = 2.00

    # Define the number of cupcakes made and sold
    cupcakes_made = 6 * 2
    cupcakes_sold = cupcakes_made - 5 - 4

    # Calculate the total cost of making the cupcakes
    total_cost = (cupcakes_made - cupcakes_sold) * COST_PER_CUPCAKE

    # Calculate the total revenue from selling the cupcakes
    total_revenue = cupcakes_sold * SELLING_PRICE_PER_CUPCAKE

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # Display the net profit
    result = net_profit
    return result

print(solution())