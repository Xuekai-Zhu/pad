def solution():
    red_car_rate = 3  # Renting a red car costs $3 for every minute
    white_car_rate = 2  # Renting a white car costs $2 for every minute
    rental_duration = 180  # All cars were rented for 3 hours, or 180 minutes

    # Calculate the total amount earned for renting red cars
    red_car_income = 3 * rental_duration * 3  # Three red cars bring in $3 per minute
    # Calculate the total amount earned for renting white cars
    white_car_income = 2 * rental_duration * 2  # Two white cars bring in $2 per minute
    # Calculate the total amount earned from all car rentals
    total_income = red_car_income + white_car_income
    result = total_income
    return result

print(solution())