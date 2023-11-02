def solution():
    # Calculate the total time taken by the first five runners to finish the race
    time_first_five = 8
    
    # Calculate the time taken by the last three runners to finish the race
    time_last_three = 8 + 2  # they finish the race 2 hours later
    
    # Calculate the total time taken by all eight runners to finish the race
    total_time = time_first_five + time_last_three
    
    result = total_time
    return result

print(solution())