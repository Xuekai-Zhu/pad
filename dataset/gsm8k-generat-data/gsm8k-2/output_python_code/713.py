def solution():
    """John runs a website that gets 30000 visits a month, for a normal 30 day month. He gets $.01 per visit. How much does he make per day?"""
    monthly_visits = 30000
    visit_pay = 0.01
    total_income = monthly_visits * visit_pay
    daily_income = total_income / 30
    result = daily_income
    return result

print(solution())