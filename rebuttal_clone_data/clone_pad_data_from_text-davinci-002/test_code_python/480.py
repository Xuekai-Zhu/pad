def solution():
    salary = 6000
    increase_percent = 30
    years_worked = 3
    total_earnings = salary * (1 + (increase_percent/100))**years_worked
    result = total_earnings
    return result

print(solution())