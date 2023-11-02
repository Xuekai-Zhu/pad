def solution():
    """Meghan had money in the following denomination: 2 $100 bills, 5 $50 bills, and 10 $10 bills. How much money did he have altogether?"""
    # Define the value of each denomination
    HUNDRED_VALUE = 100
    FIFTY_VALUE = 50
    TEN_VALUE = 10

    # Define the number of bills of each denomination
    num_hundreds = 2
    num_fifties = 5
    num_tens = 10

    # Calculate the total value of the hundreds
    hundreds_total = num_hundreds * HUNDRED_VALUE

    # Calculate the total value of the fifties
    fifties_total = num_fifties * FIFTY_VALUE

    # Calculate the total value of the tens
    tens_total = num_tens * TEN_VALUE

    # Calculate the total value of all the bills
    total_value = hundreds_total + fifties_total + tens_total

    # Display the total value
    result = total_value
    return result

print(solution())