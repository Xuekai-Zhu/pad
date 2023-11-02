def solution():
    """Lightning McQueen, the race car, cost 140000$.  Mater only cost 10 percent of that, and Sally McQueen cost triple what Mater costs.  How much does Sally McQueen cost?"""
    # Define the cost of Lightning McQueen and the ratio of costs between characters
    lightning_cost = 140000
    mater_ratio = 0.1
    sally_ratio = 3

    # Calculate the cost of Mater
    mater_cost = lightning_cost * mater_ratio

    # Calculate the cost of Sally McQueen
    sally_cost = mater_cost * sally_ratio

    # Display the cost of Sally McQueen
    result = sally_cost
    return result

print(solution())