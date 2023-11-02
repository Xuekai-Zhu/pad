def solution():
    daily_pay = 10
    num_days = 30
    num_sundays = 4
    total_days = num_days - num_sundays
    
    payment = daily_pay * total_days
    expenses = 50 * 2  # for books and giving to sister
    remaining_money = payment - expenses
    result = remaining_money
    return result

print(solution())