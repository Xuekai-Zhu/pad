def solution():
    windows_per_floor = 3  # Each floor has 3 windows
    num_floors = 3  # Lucas lives in a 3-story house
    total_windows = windows_per_floor * num_floors  # Total windows in the house
    days_passed = 6  # Lucas finished the job in 6 days
    window_payment = 2  # Lucas gets paid $2 per window
    late_penalty = 1  # Lucas loses $1 for every 3 days that pass without finishing the job
    days_late = days_passed - 3  # Get the number of days late, if any
    
    # Calculate the payment for cleaning all the windows
    payment = total_windows * window_payment
    
    # Apply a penalty for each 3 days late
    if days_late > 0:
        penalty = (days_late // 3) * late_penalty
        payment -= penalty
    
    result = payment
    return result

print(solution())