def solution():
    cars_per_day = 80
    revenue_per_car = 5
    num_days = 5

    # Calculate the total number of cars cleaned in 5 days
    total_cars_cleaned = cars_per_day * num_days

    # Calculate the total revenue generated in 5 days
    total_revenue = total_cars_cleaned * revenue_per_car
    result = total_revenue
    return result

print(solution())