def solution():
    # Convert the time limit from minutes to hours
    time_limit_hours = 10/60  # 10 minutes = 10/60 hours
    
    # Calculate the required speed in miles per hour
    required_speed = 5 / time_limit_hours
    
    result = required_speed
    return result

print(solution())