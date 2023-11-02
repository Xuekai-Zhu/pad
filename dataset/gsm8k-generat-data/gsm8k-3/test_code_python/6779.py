def solution():
    """Mandy has three $20 bills while Manny has two $50 bills. If both of them decide to exchange their bills for $10 bills, how many more $10 bills than Mandy will Manny have?"""
    # Define the value of each bill
    MANDY_BILL_VALUE = 20
    MANNY_BILL_VALUE = 50
    NEW_BILL_VALUE = 10

    # Define the number of bills each person has
    mandy_bills = 3
    manny_bills = 2

    # Calculate the total value of each person's bills
    mandy_value = mandy_bills * MANDY_BILL_VALUE
    manny_value = manny_bills * MANNY_BILL_VALUE

    # Calculate the total number of $10 bills each person will receive
    mandy_new_bills = mandy_value // NEW_BILL_VALUE
    manny_new_bills = manny_value // NEW_BILL_VALUE

    # Calculate the difference in the number of $10 bills each person will have
    difference = manny_new_bills - mandy_new_bills

    # Display the difference
    result = difference
    return result

print(solution())