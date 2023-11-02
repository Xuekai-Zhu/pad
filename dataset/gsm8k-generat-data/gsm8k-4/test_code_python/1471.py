def solution():
    """Karen's class fund contains only $10 and $20 bills, which amount to $120. The number of $10 bills is twice as many $20 bills. How many $20 bills do they have in their fund?"""
    # Define the value of a $10 bill and a $20 bill
    TEN_BILL_VALUE = 10
    TWENTY_BILL_VALUE = 20

    # Define the total amount of money in the fund and the number of $20 bills
    total_money = 120
    twenty_bills = None

    # Calculate the number of $10 bills
    ten_bills = (total_money - 2 * TWENTY_BILL_VALUE) / (TEN_BILL_VALUE - TWENTY_BILL_VALUE)

    # Calculate the number of $20 bills
    twenty_bills = (total_money - ten_bills * TEN_BILL_VALUE) / TWENTY_BILL_VALUE

    result = round(twenty_bills)
    return result

print(solution())