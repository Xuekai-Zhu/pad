def solution():
    """Oliver has 10 $20 and 3 $5 bills. William has 15 $10 and 4 $5 bills. How much more money does Oliver have than William?"""
    # Calculate the total amount of money Oliver has
    oliver_money = (10 * 20) + (3 * 5)

    # Calculate the total amount of money William has
    william_money = (15 * 10) + (4 * 5)

    # Calculate the difference in money between Oliver and William
    difference = oliver_money - william_money

    # return the result
    result = difference
    return result

print(solution())