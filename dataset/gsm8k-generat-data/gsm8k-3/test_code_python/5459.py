def solution():
    """The bus driver drives an average of 2 hours each day, 5 days a week. From Monday to Wednesday he drove at an average speed of 12 kilometers per hour, and from Thursday to Friday at an average speed of 9 kilometers per hour. How many kilometers did the driver travel during these 5 days?"""
    
    # Define the average driving hours per day
    AVG_DRIVING_HOURS = 2
    
    # Define the average speed for the first 3 days and the last 2 days
    SPEED1 = 12
    SPEED2 = 9
    
    # Calculate the total driving time for the week
    total_driving_time = AVG_DRIVING_HOURS * 5
    
    # Calculate the total distance driven from Monday to Wednesday
    distance1 = SPEED1 * total_driving_time * 3
    
    # Calculate the total distance driven from Thursday to Friday
    distance2 = SPEED2 * total_driving_time * 2
    
    # Calculate the total distance driven for the week
    total_distance = distance1 + distance2
    
    # Display the total distance driven
    result = total_distance
    return result

print(solution())