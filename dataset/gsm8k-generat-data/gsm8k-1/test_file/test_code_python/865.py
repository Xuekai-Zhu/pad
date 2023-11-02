def solution():
    """An electronics seller bought 5 phones for $700 each and gives the seller $4000 in dollar bills. How much will the seller give back in change?"""
    phone_cost = 700
    num_phones = 5
    total_cost = phone_cost * num_phones
    cash_provided = 4000
    change = cash_provided - total_cost
    result = change
    return result

print(solution())