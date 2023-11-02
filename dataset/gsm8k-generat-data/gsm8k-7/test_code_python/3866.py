def solution():
    num_bikes_added_per_week = 3
    num_weeks_in_month = 4
    num_bikes_sold_in_month = 18
    num_bikes_remaining_after_month = 45
    
    # Calculate the total number of bikes added during the month
    total_bikes_added = num_bikes_added_per_week * num_weeks_in_month
    
    # Calculate the original number of bikes
    original_num_bikes = total_bikes_added + num_bikes_sold_in_month + num_bikes_remaining_after_month
    result = original_num_bikes
    return result

print(solution())