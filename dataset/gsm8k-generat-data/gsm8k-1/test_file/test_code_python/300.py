def solution():
    """Watson works a 10-hour shift each day, five days a week. He earns $10 per hour and gets a $300 bonus each week if the company performs well. How much money did Watson make in April if the company performed very well for the whole month?"""
    daily_salary = 10 * 10
    weekly_salary = daily_salary * 5
    total_salary = weekly_salary * 4
    bonus = 300 * 4
    total_earnings = total_salary + bonus
    result = total_earnings
    return result

print(solution())