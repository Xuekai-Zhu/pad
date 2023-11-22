def solution():
    
    salary = 6000
    rent = salary / 4
    car_fuel = salary / 3
    remaining_salary = salary - rent - car_fuel
    donated_charity = remaining_salary / 2
    total_expenses = 200
    total_donated = 700
    total_expenses += donated_charity
    total_remaining = remaining_salary - total_expenses - total_donated
    result = total_remaining
    return result

print(solution())