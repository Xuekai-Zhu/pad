def solution():
    """Mandy has three $20 bills while Manny has two $50 bills. If both of them decide to exchange their bills for $10 bills, how many more $10 bills than Mandy will Manny have?"""
    # Define the initial value of Mandy's and Manny's bills
    mandy_bills = 3 * 20
    manny_bills = 2 * 50

    # Calculate the total value of bills they have
    total_bills = mandy_bills + manny_bills

    # Calculate the total number of $10 bills they can get
    total_10_bills = total_bills // 10

    # Calculate the number of $10 bills Mandy can get
    mandy_10_bills = mandy_bills // 10

    # Calculate the number of $10 bills Manny can get
    manny_10_bills = manny_bills // 10

    # Calculate the difference between Manny's and Mandy's $10 bills
    difference = manny_10_bills - mandy_10_bills

    # Return the result
    result = difference
    return result

print(solution())