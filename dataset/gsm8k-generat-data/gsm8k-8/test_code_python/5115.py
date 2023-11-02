def solution():
    # Define the variables
    hourly_pay_rate = 20
    weekly_hours = 52
    overtime_hours = weekly_hours - 40
    overtime_pay_rate = hourly_pay_rate * 1.5
    car_cost = 4640

    # Calculate the total pay for one week
    regular_pay = hourly_pay_rate * 40
    overtime_pay = overtime_hours * overtime_pay_rate
    total_pay = regular_pay + overtime_pay

    # Calculate the number of weeks needed to purchase the car
    weeks_to_purchase = car_cost / total_pay
    result = weeks_to_purchase
    return result

print(solution())