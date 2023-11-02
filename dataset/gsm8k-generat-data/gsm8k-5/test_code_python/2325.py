def solution():
    cost_of_car = 5  # One little car costs $5
    total_cars_sold = 3  # George sold 3 little cars
    total_earnings = 45  # George earned $45 in total

    # Calculate the total cost of the little cars sold
    cost_of_cars_sold = cost_of_car * total_cars_sold

    # Calculate the cost of the Legos set
    cost_of_legos = total_earnings - cost_of_cars_sold
    result = cost_of_legos
    return result

print(solution())