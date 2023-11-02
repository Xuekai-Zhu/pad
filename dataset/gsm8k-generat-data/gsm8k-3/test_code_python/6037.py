def solution():
    """James finds 3 bills in his pocket.  They are all 20s.  If he already had $75 in his wallet how much money doe he have now?"""
    # Define the value of each bill
    BILL_VALUE = 20

    # Define the number of bills found
    num_bills = 3

    # Calculate the total value of the bills found
    found_value = num_bills * BILL_VALUE

    # Calculate James' new total amount of money
    total_money = found_value + 75

    # Display James' new total amount of money
    result = total_money
    return result

print(solution())