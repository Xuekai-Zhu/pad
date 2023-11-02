def solution():
    nickel_atomic_number = 28
    mercury_atomic_number = 80
    dollar_per_atomic_number = 1
    nickel_payout = nickel_atomic_number * dollar_per_atomic_number
    mercury_payout = mercury_atomic_number * dollar_per_atomic_number
    if nickel_payout > mercury_payout:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())