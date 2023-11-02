def solution():
    days_worked = 10
    amount = 250
    desired_amount = amount * 2
    day_increment = 1
    while amount < desired_amount:
        amount += day_increment
        days_worked += 1
    result = days_worked
    return result

print(solution())