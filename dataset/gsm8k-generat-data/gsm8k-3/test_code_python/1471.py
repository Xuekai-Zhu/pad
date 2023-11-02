def solution():
    """Karen's class fund contains only $10 and $20 bills,  which amount to $120. The number of $10 bills is twice as many $20 bills. How many $20 bills do they have in their fund?"""
    # Define the value of a $10 bill and a $20 bill
    TEN_VALUE = 10
    TWENTY_VALUE = 20

    # Define the total value of the class fund
    total_value = 120

    # Calculate the number of $10 bills in the fund
    num_ten_bills = (total_value - TWENTY_VALUE * x) / TEN_VALUE
    # Solve for x using the equation: num_ten_bills = 2 * num_twenty_bills
    x = num_ten_bills / 2

    # Calculate the number of $20 bills in the fund
    num_twenty_bills = x

    result = num_twenty_bills
    return result

print(solution())