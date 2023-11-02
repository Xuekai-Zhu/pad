def solution():
    normal_hourly_rate = 500/40
    overtime_hourly_rate = normal_hourly_rate + 20

    normal_income = normal_hourly_rate * 40
    overtime_income = overtime_hourly_rate * 10

    total_income = normal_income + overtime_income

    return total_income

print(solution())