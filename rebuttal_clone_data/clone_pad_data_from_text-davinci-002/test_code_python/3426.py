def solution():
    initial_bills = 2
    bills_to_fifties = 1
    bills_remaining = initial_bills - bills_to_fifties
    bills_to_tens = bills_remaining / 2
    bills_to_fives = bills_remaining - bills_to_tens
    total_bills = initial_bills + bills_to_fifties + bills_to_tens + bills_to_fives
    result = total_bills
    return result

print(solution())