def solution():
    red_cars = 3
    white_cars = 2
    red_car_cost = 3
    white_car_cost = 2
    hours_rented = 3
    minutes_rented = hours_rented * 60
    red_car_revenue = red_cars * minutes_rented * red_car_cost
    white_car_revenue = white_cars * minutes_rented * white_car_cost
    total_revenue = red_car_revenue + white_car_revenue
    result = total_revenue
    return result

print(solution())