def solution():
    """Gail has some bills in her wallet which amount to $100. She has four $5 bills and three $20 bills, and the rest are $10 bills. How many $10 bills are in her wallet?"""
    # Define the total amount of money Gail has
    total_amount = 100

    # Define the values of each type of bill
    FIVE_BILL = 5
    TWENTY_BILL = 20
    TEN_BILL = 10

    # Define the number of each type of bill that Gail has
    num_five_bills = 4
    num_twenty_bills = 3

    # Calculate the total value of the five and twenty dollar bills
    total_five_twenty = (num_five_bills * FIVE_BILL) + (num_twenty_bills * TWENTY_BILL)

    # Calculate the total value of the ten dollar bills
    total_ten = total_amount - total_five_twenty

    # Calculate the number of ten dollar bills Gail has
    num_ten_bills = total_ten / TEN_BILL

    # Display the number of ten dollar bills
    result = num_ten_bills
    return result

print(solution())