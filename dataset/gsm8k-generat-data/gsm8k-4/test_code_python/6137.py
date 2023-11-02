def solution():
    """Lori owns a carsharing company. There are three red cars and two white cars available to rent. Renting the white car costs $2 for every minute and the red car $3 for every minute. All cars were rented for 3 hours. How much money did Lori earn?"""
    # Define the number of red and white cars
    red_cars = 3
    white_cars = 2

    # Define the rental prices for red and white cars
    red_price = 3
    white_price = 2

    # Define the rental duration in minutes
    rental_duration = 3 * 60

    # Calculate the total earnings from renting red cars
    red_earnings = red_cars * rental_duration * red_price

    # Calculate the total earnings from renting white cars
    white_earnings = white_cars * rental_duration * white_price

    # Calculate the total earnings from all cars
    total_earnings = red_earnings + white_earnings

    # return the result
    result = total_earnings
    return result

print(solution())