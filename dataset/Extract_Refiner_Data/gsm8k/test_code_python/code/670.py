def solution():
    
    # Define the height increase in inches per day
    height_increase_per_day = 30

    # Define the current height in inches
    current_height = 20 * 12

    # Define the target height in inches
    target_height = 600

    # Calculate the number of days it will take to reach the target height
    days = (target_height - current_height) / height_increase_per_day

    # Display the number of days
    result = days
    return result

print(solution())