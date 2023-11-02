def solution():
    month_income = 2500
    rent = 700
    car_payment = 300
    utilities = car_payment / 2
    groceries = 50
    remaining = month_income - rent - car_payment - utilities - groceries
    retirement = remaining / 2
    final = remaining - retirement
    result = final
    return result

print(solution())