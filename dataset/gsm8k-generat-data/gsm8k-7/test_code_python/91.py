def solution():
    base_pay = 80
    bonus_pay = 20
    base_hours = 8
    bonus_hours = 10

    # Calculate the hourly rate for base pay
    hourly_rate_base = base_pay / base_hours

    # Calculate the hourly rate for bonus pay
    hourly_rate_bonus = (base_pay + bonus_pay) / bonus_hours

    result = hourly_rate_bonus
    return result

print(solution())