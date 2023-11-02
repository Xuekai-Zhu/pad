def solution():
    
    hourly_rate = 40
    hours_per_day = 8
    days_per_week = 5
    old_bills = 600
    personal_trainer = 100
    new_rate = hourly_rate * 1.05
    new_weekly_income = new_rate * hours_per_day * days_per_week
    new_weekly_expenses = old_bills + personal_trainer
    leftover_money = new_weekly_income - new_weekly_expenses
    result = leftover_money
    return result

print(solution())