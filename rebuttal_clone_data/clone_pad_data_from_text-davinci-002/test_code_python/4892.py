def solution():
    trip_cost = 7000
    bill_cost = 3500
    savings_per_month = 500
    savings_total = savings_per_month * 24
    result = savings_total - trip_cost - bill_cost
    return result

print(solution())