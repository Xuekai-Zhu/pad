def solution():
    """Mr. Isaac rides his bicycle at the rate of 10 miles per hour for 30 minutes. If he rides for another 15 miles, rests for 30 minutes, and then covers the remaining distance of 20 miles, what's the total time in minutes took to travel the whole journey?"""
    # Calculate the time taken to ride the first 5 miles
    time1 = 30 / 60
    
    # Calculate the time taken to ride the next 15 miles
    time2 = 15 / 10
    
    # Calculate the time taken to rest
    rest_time = 30
    
    # Calculate the time taken to ride the last 20 miles
    time3 = 20 / 10
    
    # Calculate the total time taken
    total_time = time1 + time2 + (rest_time / 60) + time3
    
    # Convert the total time to minutes
    total_time_minutes = total_time * 60
    
    # Round the result to the nearest minute
    result = round(total_time_minutes)
    return result

print(solution())