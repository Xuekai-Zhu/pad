def solution():
    total_amount = 100
    num_5_bills = 4
    num_20_bills = 3

    # Calculate the total value of the $5 bills
    total_5_bills_value = num_5_bills * 5

    # Calculate the total value of the $20 bills
    total_20_bills_value = num_20_bills * 20

    # Calculate the remaining amount (excluding the $5 and $20 bills)
    remaining_amount = total_amount - total_5_bills_value - total_20_bills_value

    # Calculate the number of $10 bills
    num_10_bills = remaining_amount / 10
    result = num_10_bills
    return result

print(solution())