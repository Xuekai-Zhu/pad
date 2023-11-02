def solution():
    """Jacob is building ladders. One of his clients needs 10 ladders with 50 rungs, and 20 ladders with 60 rungs. Jacob has to charge $2 for every rung. How much does the client have to pay for the ladders?"""
    # Define the price per rung
    PRICE_PER_RUNG = 2

    # Define the number of ladders with 50 rungs and 60 rungs
    num_ladders_50_rungs = 10
    num_ladders_60_rungs = 20

    # Calculate the total number of rungs
    total_rungs = num_ladders_50_rungs * 50 + num_ladders_60_rungs * 60

    # Calculate the total cost
    total_cost = total_rungs * PRICE_PER_RUNG

    # Display the total cost
    result = total_cost
    return result

print(solution())