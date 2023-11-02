def solution():
    # Calculate the total cost for renting the white cars for 3 hours
    white_cars_cost = 2 * 60 * 3 * 2  # $2 per minute for 3 hours for 2 white cars

    # Calculate the total cost for renting the red cars for 3 hours
    red_cars_cost = 3 * 60 * 3 * 3  # $3 per minute for 3 hours for 3 red cars

    # Calculate the total amount of money earned by Lori
    total_earned = white_cars_cost + red_cars_cost
    result = total_earned
    return result

print(solution())