def solution():
    num_customers_per_hour = 10
    num_hours_worked = 8
    bonus_percentage = 0.2

    # Calculate the total number of customers served
    total_customers_served = num_customers_per_hour * num_hours_worked

    # Calculate the total number of bonus points earned
    total_bonus_points = total_customers_served * bonus_percentage
    result = total_bonus_points
    return result

print(solution())