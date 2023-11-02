def solution():
    
    annual_salary = 40000
    taxes = annual_salary * 0.2
    healthcare = annual_salary * 0.1
    union_dues = 800
    take_home_pay = annual_salary - taxes - healthcare - union_dues
    result = take_home_pay
    return result

print(solution())