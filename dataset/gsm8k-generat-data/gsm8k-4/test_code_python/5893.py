def solution():
    """Mary, Jess, and Christina want to decorate a party room with balloons. Each person inflates balloons at different speeds, and they only have 30 minutes to inflate as many balloons as possible. Mary inflates 10 balloons per minute, Jess inflates 7 balloons per minute and Christina came 15 minutes late and was the slowest one inflating 4 balloons per minute. How many balloons can they inflate before running out of time?"""
    
    # Define the time they have to inflate the balloons in minutes
    time_in_minutes = 30
    
    # Define the number of balloons each person can inflate per minute
    balloons_per_minute = {'Mary': 10, 'Jess': 7, 'Christina': 4}
    
    # Define the total number of balloons each person can inflate in 30 minutes
    total_balloons = {}
    for name, speed in balloons_per_minute.items():
        if name == 'Christina':
            speed = 4 # Christina was late and only had 15 minutes
            time = time_in_minutes - 15
        else:
            time = time_in_minutes
        total_balloons[name] = speed * time
        
    # Calculate the total number of balloons they can inflate together
    total = sum(total_balloons.values())
    
    # Return the result
    return total

print(solution())