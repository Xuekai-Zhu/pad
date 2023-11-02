def solution():
    """Jacob is building ladders. One of his clients needs 10 ladders with 50 rungs, and 20 ladders with 60 rungs. Jacob has to charge $2 for every rung. How much does the client have to pay for the ladders?"""
    # Define the number of ladders and rungs
    ladders_50 = 10
    rungs_50 = 50

    ladders_60 = 20
    rungs_60 = 60

    # Define the price per rung
    price_per_rung = 2

    # Calculate the total number of rungs and the cost
    total_rungs = (ladders_50 * rungs_50) + (ladders_60 * rungs_60)
    total_cost = total_rungs * price_per_rung

    # return the result
    result = total_cost
    return result

print(solution())