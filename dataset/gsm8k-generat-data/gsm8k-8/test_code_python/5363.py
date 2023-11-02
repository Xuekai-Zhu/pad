def solution():
    # Define the target amount of water to drink in liters
    target_amount = 3

    # Define the amount of water Sandy drinks every 2 hours in liters
    amount_per_interval = 0.5

    # Calculate the number of intervals needed to reach the target
    intervals_needed = target_amount / amount_per_interval

    # Calculate the total time needed in hours
    total_time_in_hours = intervals_needed * 2
    result = total_time_in_hours
    return result

print(solution())