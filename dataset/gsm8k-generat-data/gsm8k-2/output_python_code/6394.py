def solution():
    """Jacob is building ladders. One of his clients needs 10 ladders with 50 rungs, and 20 ladders with 60 rungs. Jacob has to charge $2 for every rung. How much does the client have to pay for the ladders?"""
    ladder1_rungs = 50
    ladder1_price = ladder1_rungs * 2
    ladder2_rungs = 60
    ladder2_price = ladder2_rungs * 2
    total_ladders = 10 + 20
    total_price = (ladder1_price * 10) + (ladder2_price * 20)
    result = total_price
    return result

print(solution())