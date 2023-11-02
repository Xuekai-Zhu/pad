def solution():
    """John wins an award at work. The award has a 1 time monetary reward of $5000 and a 5% raise in salary. If he makes 2000 a week, every week of the year and he got the award on the first day of the year how much money did he make that year?"""
    weekly_salary = 2000
    yearly_salary = weekly_salary * 52
    award_money = 5000
    new_salary = yearly_salary * 0.05 + yearly_salary
    total_money = new_salary + award_money
    result = total_money
    return result

print(solution())