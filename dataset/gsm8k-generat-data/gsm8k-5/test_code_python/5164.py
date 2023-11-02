def solution():
    amount_withdrawn = 300 * 2  # Tye withdraws $300 from two banks
    denomination = 20  # Tye gets the money in $20 bills

    # Calculate the number of bills Tye got
    num_bills = amount_withdrawn / denomination
    result = num_bills
    return result

print(solution())