def solution():
    hours_per_week = 40
    hourly_rate = 11.5
    total_hours_worked = hours_per_week * 2  # two weeks
    gross_pay = total_hours_worked * hourly_rate
    tire_cost = 410
    net_pay = gross_pay - tire_cost
    result = net_pay
    return result

print(solution())