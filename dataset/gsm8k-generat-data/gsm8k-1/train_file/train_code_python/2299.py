def solution():
    """Josh works 8 hours a day, 5 days a week, 4 weeks a month. Carl is an intern and works 2 hours less than Josh every day. Josh gets $9 an hour and Carl, half that. How much does the company pay for the 2 together in one month?"""
    josh_hours_per_week = 8 * 5
    carl_hours_per_week = josh_hours_per_week - 2
    josh_salary = 9 * josh_hours_per_week * 4
    carl_salary = 4 * carl_hours_per_week * (9 / 2)
    total_salary = josh_salary + carl_salary
    result = total_salary
    return result

print(solution())