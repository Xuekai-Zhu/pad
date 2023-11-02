def solution():
    """Lori owns a carsharing company. there are three red cars and two white cars available to rent. Renting the white car costs $2 for every minute and the red car $3 for every minute. All cars were rented for 3 hours. How much money did Lori earn?"""
    red_cars = 3
    white_cars = 2
    red_price = 3
    white_price = 2
    rental_time = 180 # 3 hours = 180 minutes
    red_total_price = red_cars * red_price * rental_time
    white_total_price = white_cars * white_price * rental_time
    total_earnings = red_total_price + white_total_price
    result = total_earnings
    return result

print(solution())