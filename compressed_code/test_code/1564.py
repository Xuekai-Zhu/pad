def solution():
    
    hourly_rate = 40
    raise_percent = 0.05
    weekly_hours = 8 * 5
    old_bills = 600
    personal_trainer_fee = 100
    new_hourly_rate = hourly_rate + (hourly_rate * raise_percent)
    new_weekly_income = new_hourly_rate * weekly_hours
    new_weekly_expenses = old_bills + personal_trainer_fee
    leftover = new_weekly_income - new_weekly_expenses
    result = leftover
    return result

print(solution())