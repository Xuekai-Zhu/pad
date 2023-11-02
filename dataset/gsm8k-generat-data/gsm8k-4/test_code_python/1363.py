def solution():
    """Prudence was starting a cupcake business. She figured that each cupcake cost $0.75 to make.
    The first 2 dozen that she made burnt and she had to throw them out. The next 2 came out perfectly
    and she ended up eating 5 cupcakes right away. Later that day she made 2 more dozen cupcakes and 
    decided to eat 4 more. If she sells the remaining cupcakes at $2.00 each, how much is her net profit?"""
    # Define the cost of making each cupcake and the selling price
    COST_PER_CUPCAKE = 0.75
    SELLING_PRICE = 2.0

    # Calculate the total number of cupcakes made
    total_cupcakes = (2 * 12) + (2 * 12)

    # Calculate the number of cupcakes thrown out, eaten, and remaining
    thrown_out = 2 * 12
    eaten = 5 + 4
    remaining = total_cupcakes - thrown_out - eaten

    # Calculate the cost of making the cupcakes
    total_cost = total_cupcakes * COST_PER_CUPCAKE

    # Calculate the revenue from selling the remaining cupcakes
    total_revenue = remaining * SELLING_PRICE

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # return the result
    result = net_profit
    return result

print(solution())