def solution():
    """Mrs. Brown paid her utility bills with 3 $50 bills and 2 $10 bills. How much are her utility bills?"""
    # Define the value of each bill
    FIFTY_BILL = 50
    TEN_BILL = 10

    # Calculate the total value of the three $50 bills
    fifty_total = 3 * FIFTY_BILL

    # Calculate the total value of the two $10 bills
    ten_total = 2 * TEN_BILL

    # Calculate the total value of all the bills
    total_bills = fifty_total + ten_total

    # Display the total cost
    result = total_bills
    return result

print(solution())