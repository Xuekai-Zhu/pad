def solution():
    hourly_rate = 20  # Janet makes $20 per hour
    normal_hours = 40  # Any hours worked up to 40 are considered normal hours
    overtime_rate = hourly_rate * 1.5  # Overtime hours are paid at 1.5 times the normal rate
    weekly_hours = 52  # Janet works 52 hours per week
    car_price = 4640

    # Calculate the weekly salary for normal hours
    salary_normal = hourly_rate * normal_hours

    # Calculate the weekly salary for overtime hours
    overtime_hours = weekly_hours - normal_hours
    salary_overtime = overtime_rate * overtime_hours

    # Calculate the total weekly salary
    total_salary = salary_normal + salary_overtime

    # Calculate the number of weeks needed to purchase the car
    weeks_needed = car_price / total_salary
    result = weeks_needed
    return result

print(solution())