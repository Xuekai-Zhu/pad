def solution():
    # Define the variables
    added_bikes_per_week = 3
    total_bikes_sold = 18
    bikes_left_in_stock = 45
    weeks_in_month = 4

    # Calculate the number of bikes added during the month
    bikes_added = added_bikes_per_week * weeks_in_month

    # Calculate the original number of bikes
    original_bikes = bikes_left_in_stock + total_bikes_sold - bikes_added
    result = original_bikes
    return result

print(solution())