def solution():
    customers_per_hour = 10  # Tom served 10 customers per hour
    hours_worked = 8  # Tom worked for 8 hours

    # Calculate the number of customers served by Tom
    total_customers_served = customers_per_hour * hours_worked

    # Calculate the number of bonus points earned by Tom
    bonus_points = total_customers_served * 0.2

    result = bonus_points
    return result

print(solution())