def solution():
    salary = 40000
    taxes = salary * 0.2
    healthcare = salary * 0.1
    union_dues = 800
    take_home_pay = salary - taxes - healthcare - union_dues
    result = take_home_pay
    return result

print(solution())