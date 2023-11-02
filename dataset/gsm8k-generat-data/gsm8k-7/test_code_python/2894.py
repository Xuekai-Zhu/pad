def solution():
    hours_worked = 8
    hourly_rate = 18
    total_earned = hours_worked * hourly_rate

    amount_spent = total_earned / 2

    money_left = total_earned - amount_spent
    result = money_left
    return result

print(solution())