def solution():
    """Jacob is building ladders. One of his clients needs 10 ladders with 50 rungs, and 20 ladders with 60 rungs. Jacob has to charge $2 for every rung. How much does the client have to pay for the ladders?"""
    num_ladders_1 = 10
    num_ladders_2 = 20
    rungs_per_ladder_1 = 50
    rungs_per_ladder_2 = 60
    price_per_rung = 2
    total_rungs = (num_ladders_1 * rungs_per_ladder_1) + (num_ladders_2 * rungs_per_ladder_2)
    total_price = total_rungs * price_per_rung
    result = total_price
    return result

print(solution())