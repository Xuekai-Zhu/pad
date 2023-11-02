def solution():
    num_weeks = 6
    num_visits_per_week = 1
    performance_length = 3
    price_per_hour = 5

    # Calculate the total number of visits to the theater
    total_visits = num_weeks * num_visits_per_week

    # Calculate the total cost of all visits to the theater
    total_cost = total_visits * performance_length * price_per_hour
    result = total_cost
    return result

print(solution())