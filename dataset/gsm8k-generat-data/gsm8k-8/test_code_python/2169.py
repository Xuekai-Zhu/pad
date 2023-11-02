def solution():
    # Calculate John's time to finish the race
    john_time = 5 / 15 * 60
    
    # Convert the other guy's time from minutes to hours
    other_time_hours = 23 / 60
    
    # Calculate the other guy's speed in mph
    other_speed = 5 / other_time_hours
    
    # Calculate the other guy's time to finish the race
    other_time = 5 / other_speed * 60
    
    # Calculate the difference in time between John and the other guy
    time_difference = john_time - other_time
    
    result = time_difference
    return result

print(solution())