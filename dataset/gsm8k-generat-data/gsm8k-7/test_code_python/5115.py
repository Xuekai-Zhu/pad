def solution():
    hourly_rate = 20
    normal_hours = 40
    overtime_rate = 30 # 1.5 times the normal rate
    weekly_hours = 52
    car_cost = 4640

    # Calculate weekly earnings
    weekly_salary = (hourly_rate * normal_hours) + ((weekly_hours - normal_hours) * overtime_rate)

    # Calculate the number of weeks needed to purchase the car
    num_weeks = car_cost / weekly_salary
    result = num_weeks
    return result

print(solution())