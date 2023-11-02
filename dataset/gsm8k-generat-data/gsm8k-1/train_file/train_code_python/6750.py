def solution():
    """After buying shirts worth $27 from a store, Dennis received 2 $10 bills and $3 in loose coins for his change. How much money did Dennis have initially?"""
    amount_paid = 27
    bills_received = 2
    value_of_bills = 10 * bills_received
    coins_received = 3
    total_received = value_of_bills + coins_received
    initial_amount = amount_paid + total_received
    result = initial_amount
    return result

print(solution())