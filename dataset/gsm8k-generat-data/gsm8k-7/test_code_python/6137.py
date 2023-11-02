def solution():
    num_red_cars = 3
    red_car_price_per_minute = 3

    num_white_cars = 2
    white_car_price_per_minute = 2

    rental_duration_hours = 3
    minutes_per_hour = 60

    # Calculate the total rental duration in minutes
    rental_duration_minutes = rental_duration_hours * minutes_per_hour

    # Calculate the earnings from renting the red cars
    red_car_earnings = num_red_cars * rental_duration_minutes * red_car_price_per_minute

    # Calculate the earnings from renting the white cars
    white_car_earnings = num_white_cars * rental_duration_minutes * white_car_price_per_minute

    # Calculate the total earnings
    total_earnings = red_car_earnings + white_car_earnings
    result = total_earnings
    return result

print(solution())