def solution():
    """Mark got a 5% raise at his job. Before the raise, he earned 40 dollars per hour. He works 8 hours per day for 5 days per week. His old bills used to be 600 dollars a week but he decided to add a hundred dollar a week personal trainer. How much does he have leftover a week?"""
    # Define Mark's old hourly rate, number of hours worked per week, and old weekly bills
    old_hourly_rate = 40
    hours_per_day = 8
    days_per_week = 5
    old_weekly_bills = 600

    # Calculate Mark's new hourly rate and weekly salary after the raise
    new_hourly_rate = old_hourly_rate * 1.05
    weekly_salary = new_hourly_rate * hours_per_day * days_per_week

    # Calculate Mark's new weekly bills after adding the personal trainer
    new_weekly_bills = old_weekly_bills + 100

    # Calculate Mark's weekly leftover money after deducting his bills from his salary
    weekly_leftover = weekly_salary - new_weekly_bills

    # return the result
    result = weekly_leftover
    return result

print(solution())