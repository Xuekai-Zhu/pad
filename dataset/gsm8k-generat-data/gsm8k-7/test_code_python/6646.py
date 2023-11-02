def solution():
    num_50_bills = 3
    num_10_bills = 2
    bill_50_value = 50
    bill_10_value = 10

    # Calculate the total value of the $50 bills
    total_50_bills_value = num_50_bills * bill_50_value

    # Calculate the total value of the $10 bills
    total_10_bills_value = num_10_bills * bill_10_value

    # Calculate the total amount paid for utility bills
    total_amount_paid = total_50_bills_value + total_10_bills_value
    result = total_amount_paid
    return result

print(solution())