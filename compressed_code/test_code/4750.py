def solution():
    
    red_car_rental_rate = 3
    white_car_rental_rate = 2
    rental_time = 3 * 60
    total_red_cars = 3
    total_white_cars = 2
    total_earned = (total_red_cars * red_car_rental_rate * rental_time) + (total_white_cars * white_car_rental_rate * rental_time)
    result = total_earned
    return result

print(solution())