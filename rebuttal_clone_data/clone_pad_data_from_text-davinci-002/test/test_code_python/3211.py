def solution():
    pay = 500
    tax = 10
    take_home_pay = pay - (pay * (tax / 100))
    result = take_home_pay
    return result

print(solution())