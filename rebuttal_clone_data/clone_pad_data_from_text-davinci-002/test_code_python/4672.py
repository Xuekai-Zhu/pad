def solution():
    hourly_rate = 20
    Monday_hours = 5 * 1.5
    Tuesday_hours = 3
    Thursday_hours = 2 * 2
    Saturday_hours = 6
    total_hours = Monday_hours + Tuesday_hours + Thursday_hours + Saturday_hours
    total_money = hourly_rate * total_hours
    result = total_money
    return result

print(solution())