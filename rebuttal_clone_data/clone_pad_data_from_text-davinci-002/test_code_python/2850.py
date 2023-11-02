def solution():
    monthly_income = 2000
    transport_percentage = 5
    transport_cost = monthly_income * (transport_percentage / 100)
    monthly_spending = monthly_income + transport_cost
    result = monthly_spending
    return result

print(solution())