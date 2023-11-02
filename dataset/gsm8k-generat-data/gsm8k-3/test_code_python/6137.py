def solution():
    """Lori owns a carsharing company. There are three red cars and two white cars available to rent. Renting the white car costs $2 for every minute and the red car $3 for every minute. All cars were rented for 3 hours. How much money did Lori earn?"""
    # Define the number of red and white cars available
    red_cars = 3
    white_cars = 2

    # Define the rental rates per minute for each color car
    red_rate = 3
    white_rate = 2

    # Calculate the total minutes all cars were rented for
    total_minutes = 3 * 60 # 3 hours * 60 minutes per hour

    # Calculate the total rental cost for the red cars
    red_cost = red_cars * red_rate * total_minutes

    # Calculate the total rental cost for the white cars
    white_cost = white_cars * white_rate * total_minutes

    # Calculate the total amount earned by Lori
    total_earnings = red_cost + white_cost

    # Display the total earnings
    result = total_earnings
    return result

print(solution())