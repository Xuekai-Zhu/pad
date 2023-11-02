def solution():
    rental_hours_per_day = 2
    num_days = 3
    cost_per_hour = 75

    # Calculate the total rental hours
    total_rental_hours = rental_hours_per_day * num_days

    # Calculate the total cost of the rental
    total_cost = total_rental_hours * cost_per_hour
    result = total_cost
    return result

print(solution())