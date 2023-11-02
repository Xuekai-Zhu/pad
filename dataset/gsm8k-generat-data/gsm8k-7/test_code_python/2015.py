def solution():
    hourly_wage_before_raise = 40
    daily_hours_worked = 8
    num_days_per_week = 5
    old_weekly_bills = 600
    personal_trainer_cost = 100
    raise_percentage = 0.05

    # Calculate Mark's new hourly wage after the raise
    hourly_wage_after_raise = hourly_wage_before_raise * (1 + raise_percentage)

    # Calculate Mark's new weekly salary after the raise
    weekly_salary_after_raise = hourly_wage_after_raise * daily_hours_worked * num_days_per_week

    # Calculate Mark's new weekly bills
    new_weekly_bills = old_weekly_bills + personal_trainer_cost

    # Calculate Mark's leftover money each week after the raise and bills
    leftover_money = weekly_salary_after_raise - new_weekly_bills
    result = leftover_money
    return result

print(solution())