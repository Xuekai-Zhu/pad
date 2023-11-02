def solution():
    """Mark got a 5% raise at his job. Before the raise, he earned 40 dollars per hour. He works 8 hours per day for 5 days per week. His old bills used to be 600 dollars a week but he decided to add a hundred dollar a week personal trainer. How much does he have leftover a week?"""
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