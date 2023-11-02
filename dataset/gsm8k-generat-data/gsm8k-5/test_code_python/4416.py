def solution():
    rental_days = 11  # Jennie rented the car for 11 days
    weekly_rental = 190  # The weekly rental fee for rentals lasting a week or longer
    daily_rental = 30  # The daily rental fee

    if rental_days >= 7:
        # If Jennie rented the car for a week or longer, she pays the weekly rental fee
        total_cost = weekly_rental + ((rental_days - 7) * daily_rental)
    else:
        # If Jennie rented the car for less than a week, she pays the daily rental fee for each day
        total_cost = rental_days * daily_rental

    result = total_cost
    return result

print(solution())