def solution():
    """Oliver has 10 $20 and 3 $5 bills. William has 15 $10 and 4 $5 bills. How much more money does Oliver have than William?"""
    # Calculate Oliver's total amount of money
    oliver_money = (10 * 20) + (3 * 5)

    # Calculate William's total amount of money
    william_money = (15 * 10) + (4 * 5)

    # Calculate the difference in their money
    difference = oliver_money - william_money

    # Display the difference in their money
    result = difference
    return result

print(solution())