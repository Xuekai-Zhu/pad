def solution():
    # Calculate the time Jenna spends driving
    jenna_time = 200 / 50
    
    # Calculate the time her friend spends driving
    friend_time = 100 / 20
    
    # Calculate the total driving time
    total_time = jenna_time + friend_time
    
    # Add the time spent on breaks (1 hour total)
    total_time += 1
    
    result = total_time
    return result

print(solution())