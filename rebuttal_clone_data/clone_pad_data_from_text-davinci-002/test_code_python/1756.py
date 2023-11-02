def solution():
    rent = 1200
    groceries = 400
    medical = 200
    utilities = 60
    savings = 200
    monthly_expenses = rent + groceries + medical + utilities + savings
    hourly_wage = 15
    hours_needed = monthly_expenses / hourly_wage
    result = hours_needed
    return result

print(solution())