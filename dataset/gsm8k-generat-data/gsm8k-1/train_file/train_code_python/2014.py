def solution():
    """Mark got a 5% raise at his job. Before the raise, he earned 40 dollars per hour. He works 8 hours per day for 5 days per week. His old bills used to be 600 dollars a week but he decided to add a hundred dollar a week personal trainer. How much does he have leftover a week?"""
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