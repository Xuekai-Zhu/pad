def solution():
    hourly_pay = 20  # dollars per hour
    regular_hours = 40  # hours per week
    overtime_pay = 1.5 * hourly_pay  # dollars per hour for overtime
    total_hours = 52  # hours per week
    car_cost = 4640  # dollars
    regular_pay = hourly_pay * regular_hours  # dollars per week for regular hours
    overtime_hours = total_hours - regular_hours  # hours of overtime per week
    overtime_pay_weekly = overtime_pay * overtime_hours  # dollars per week for overtime pay
    weekly_pay = regular_pay + overtime_pay_weekly  # dollars per week for total pay
    
    # Calculate the number of weeks needed to purchase the car
    num_weeks = car_cost / weekly_pay
    result = num_weeks
    return result

print(solution())