def solution():
    total_cents = 123 + 85 + 35
    trip_cost = 15
    leftover_cents = 48
    needed_cents = trip_cost - leftover_cents
    quarters = needed_cents / 25
    result = quarters
    return result

print(solution())