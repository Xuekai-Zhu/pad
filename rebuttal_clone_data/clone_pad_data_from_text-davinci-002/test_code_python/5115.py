def solution():
    regular_pay_per_hour = 20
    regular_hours_per_week = 40
    overtime_pay_per_hour = regular_pay_per_hour * 1.5
    overtime_hours_per_week = 52 - regular_hours_per_week
    total_hours_per_week = regular_hours_per_week + overtime_hours_per_week
    car_cost = 4640
    weekly_earnings = (regular_hours_per_week * regular_pay_per_hour) + (overtime_hours_per_week * overtime_pay_per_hour)
    number_of_weeks = car_cost / weekly_earnings
    result = number_of_weeks
    return result

print(solution())