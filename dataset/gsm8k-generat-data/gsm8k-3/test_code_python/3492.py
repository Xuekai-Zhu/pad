def solution():
    """Samuel has $5, $10, and $20 bills which amount to $150 in his wallet. His $10-bills amount to $50, and he has 4 $20-bills. How many bills does Samuel have in his wallet?"""
    # Define the value of each type of bill
    FIVE_VALUE = 5
    TEN_VALUE = 10
    TWENTY_VALUE = 20

    # Define the total amount of money in Samuel's wallet
    total_amount = 150

    # Define the number of $10 bills Samuel has
    num_ten_bills = 5

    # Define the number of $20 bills Samuel has
    num_twenty_bills = 4

    # Calculate the number of $5 bills Samuel has
    num_five_bills = (total_amount - num_ten_bills*TEN_VALUE - num_twenty_bills*TWENTY_VALUE) / FIVE_VALUE

    # Calculate the total number of bills Samuel has
    total_num_bills = num_five_bills + num_ten_bills + num_twenty_bills

    # Display the total number of bills
    result = total_num_bills
    return result

print(solution())