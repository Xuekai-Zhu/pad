def solution():
    """Mrs. Oaklyn buys handmade rugs at $40 each and sells them at $60 each. 
    If she bought 20 rugs, calculate the profit she will make from selling the rugs."""
    # Define the cost price and selling price of each handmade rug
    CP = 40
    SP = 60

    # Define the number of handmade rugs bought
    n_rugs = 20

    # Calculate the total cost of buying the handmade rugs
    total_cost = CP * n_rugs

    # Calculate the total revenue from selling the handmade rugs
    total_revenue = SP * n_rugs

    # Calculate the profit from selling the handmade rugs
    profit = total_revenue - total_cost

    # return the result
    result = profit
    return result

print(solution())