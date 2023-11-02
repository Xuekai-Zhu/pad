def solution():
    """Tim gets a promotion that offers him a 5% raise on his $20000 a month salary. It also gives him a bonus worth half a month's salary. How much money will he make in a year?"""
    monthly_salary = 20000
    raise_percent = 5
    bonus_percent = 50
    raise_amount = monthly_salary * (raise_percent/100)
    bonus_amount = monthly_salary * (bonus_percent/100)
    new_salary = monthly_salary + raise_amount + bonus_amount
    yearly_salary = new_salary * 12
    result = yearly_salary
    return result

print(solution())