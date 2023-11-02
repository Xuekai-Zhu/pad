def solution():
    amount_withdrawn = 300

    # Calculate the number of bills Tye received from each bank
    num_bills_per_bank = amount_withdrawn / 20

    # Calculate the total number of bills that Tye received
    total_bills = num_bills_per_bank * 2

    result = total_bills
    return result

print(solution())