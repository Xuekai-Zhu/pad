def solution():
    """Steve makes 40000$ a year as a teacher. He loses 20 percent to taxes, 10 percent to healthcare, and 800$ to local union dues. How much money does Steve take home?"""
    annual_salary = 40000
    taxes = annual_salary * 0.2
    healthcare = annual_salary * 0.1
    union_dues = 800
    take_home_pay = annual_salary - taxes - healthcare - union_dues
    result = take_home_pay
    return result

print(solution())