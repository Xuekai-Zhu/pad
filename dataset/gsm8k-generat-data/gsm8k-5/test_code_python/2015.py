def solution():
    old_hourly_pay = 40  # Mark earned $40 per hour before the raise
    new_hourly_pay = old_hourly_pay * 1.05  # Mark got a 5% raise, so his new hourly pay is 105% of his old hourly pay
    hours_per_day = 8  # Mark works 8 hours per day
    days_per_week = 5  # Mark works 5 days per week
    old_bills = 600  # Mark used to spend $600 per week on bills
    personal_trainer_cost = 100  # Mark now spends $100 per week on a personal trainer

    # Calculate Mark's new hourly pay and his new weekly salary
    new_weekly_salary = new_hourly_pay * hours_per_day * days_per_week

    # Calculate Mark's new weekly expenses
    new_expenses = old_bills + personal_trainer_cost

    # Calculate Mark's leftover money each week
    leftover_money = new_weekly_salary - new_expenses
    result = leftover_money
    return result

print(solution())