def solution():
    """Meghan had money in the following denomination: 2 $100 bills, 5 $50 bills, and 10 $10 bills. How much money did he have altogether?"""
    # Define the value of each denomination
    value_100 = 100
    value_50 = 50
    value_10 = 10

    # Calculate the total value of the $100 bills
    total_100 = value_100 * 2

    # Calculate the total value of the $50 bills
    total_50 = value_50 * 5

    # Calculate the total value of the $10 bills
    total_10 = value_10 * 10

    # Calculate the total amount of money
    total_money = total_100 + total_50 + total_10

    # Return the result
    result = total_money
    return result

print(solution())