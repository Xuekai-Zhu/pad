def solution():
    
    rental_frequency = 10
    rental_hours_per_month = 3
    rental_pay_per_hour = 25
    car_payment = 500
    total_rental_hours = rental_frequency * rental_hours_per_month * 12
    total_rental_pay = total_rental_hours * rental_pay_per_hour
    profit = car_payment - total_rental_pay
    result = profit
    return result

print(solution())