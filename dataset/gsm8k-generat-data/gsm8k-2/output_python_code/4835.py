def solution():
    """Jon runs a website where he gets paid for every person who visits. He gets paid $0.10 for every person who visits. Each hour he gets 50 visits. His website operates 24 hours a day. How many dollars does he make in a 30 day month?"""
    visits_per_hour = 50
    hours_per_day = 24
    days_per_month = 30
    visit_pay = 0.10
    total_visits = visits_per_hour * hours_per_day * days_per_month
    total_income = total_visits * visit_pay
    result = total_income
    return result

print(solution())