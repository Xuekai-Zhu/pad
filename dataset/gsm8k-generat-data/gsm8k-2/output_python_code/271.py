def solution():
    """Oliver has 10 $20 and 3 $5 bills. William has 15 $10 and 4 $5 bills. How much more money does Oliver have than William?"""
    oliver_money = (10 * 20) + (3 * 5)
    william_money = (15 * 10) + (4 * 5)
    difference = oliver_money - william_money
    result = difference
    return result

print(solution())