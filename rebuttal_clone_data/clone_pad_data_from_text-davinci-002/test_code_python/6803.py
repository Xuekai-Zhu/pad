def solution():
    revenue = 4000
    expenses = 1500
    initial_cost = 25000
    month_payback = initial_cost / (revenue - expenses)
    result = month_payback
    return result

print(solution())