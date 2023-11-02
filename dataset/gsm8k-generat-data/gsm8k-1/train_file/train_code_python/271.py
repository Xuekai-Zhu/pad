def solution():
    """Oliver has 10 $20 and 3 $5 bills. William has 15 $10 and 4 $5 bills. How much more money does Oliver have than William?"""
    oliver_cash = (10 * 20) + (3 * 5)
    william_cash = (15 * 10) + (4 * 5)
    difference = oliver_cash - william_cash
    result = difference
    return result

print(solution())