def solution():
    """Lori owns a carsharing company. There are three red cars and two white cars available to rent. Renting the white car costs $2 for every minute and the red car $3 for every minute. All cars were rented for 3 hours. How much money did Lori earn?"""
    red_car_rental_rate = 3
    white_car_rental_rate = 2
    rental_time = 3 * 60
    total_red_cars = 3
    total_white_cars = 2
    total_earned = (total_red_cars * red_car_rental_rate * rental_time) + (total_white_cars * white_car_rental_rate * rental_time)
    result = total_earned
    return result

print(solution())