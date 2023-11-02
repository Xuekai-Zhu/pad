def solution():
    bills_found = 3  # James found 3 bills
    value_of_bills = 20  # The value of each bill is $20

    # Calculate the value of the bills James found
    value_found = bills_found * value_of_bills

    # Add the value of the bills found to the amount James already had in his wallet
    total_money = value_found + 75
    result = total_money
    return result

print(solution())