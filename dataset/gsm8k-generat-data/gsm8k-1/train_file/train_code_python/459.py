def solution():
    """John gets a bonus that's the same percentage every year. Last year he made $100,000 and got a $10,000 bonus. 
    This year he makes $200,000. How much will John make this year when adding both his total pay and bonus together?"""
    last_year_salary = 100000
    last_year_bonus = 10000
    bonus_percentage = last_year_bonus / last_year_salary
    this_year_salary = 200000
    this_year_bonus = this_year_salary * bonus_percentage
    total_pay = this_year_salary + this_year_bonus
    result = total_pay
    return result

print(solution())