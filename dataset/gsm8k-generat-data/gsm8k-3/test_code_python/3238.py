def solution():
    """Jill can run up a hill at 9 feet/second and down a hill at 12 feet/second. How long does it take her to run up and down a 900 foot hill?"""
    
    # Define the distances and speeds
    distance = 900
    uphill_speed = 9
    downhill_speed = 12
    
    # Calculate the time to run uphill
    uphill_time = distance / uphill_speed
    
    # Calculate the time to run downhill
    downhill_time = distance / downhill_speed
    
    # Calculate the total time
    total_time = uphill_time + downhill_time
    
    # Display the total time
    result = total_time
    return result

print(solution())