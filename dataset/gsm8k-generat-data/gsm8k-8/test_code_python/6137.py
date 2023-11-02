def solution():
    # Define the number of red and white cars and the rental rates
    num_red_cars = 3
    num_white_cars = 2
    red_rental_rate = 3
    white_rental_rate = 2

    # Calculate the total rental time in minutes
    rental_time_in_hours = 3
    rental_time_in_minutes = rental_time_in_hours * 60

    # Calculate the total revenue from red car rentals
    red_revenue = num_red_cars * red_rental_rate * rental_time_in_minutes

    # Calculate the total revenue from white car rentals
    white_revenue = num_white_cars * white_rental_rate * rental_time_in_minutes

    # Calculate the total revenue from all car rentals
    total_revenue = red_revenue + white_revenue
    result = total_revenue
    return result

print(solution())