def solution():
    leave_time_hour = 17
    leave_time_minute = 0
    
    current_time_hour = 14
    current_time_minute = 30
    
    oldest_daughter_time = 45
    youngest_daughter_time = 30
    husband_time = 20
    
    # Convert all times to minutes
    current_time = current_time_hour * 60 + current_time_minute
    oldest_daughter_time = oldest_daughter_time
    youngest_daughter_time = youngest_daughter_time
    husband_time = husband_time
    
    # Calculate the total time the bathroom was occupied
    total_occupied_time = oldest_daughter_time + youngest_daughter_time + husband_time
    
    # Calculate the time Mrs. Parker has left to use the bathroom
    remaining_time = leave_time_hour * 60 + leave_time_minute - current_time - total_occupied_time
    result = remaining_time
    return result

print(solution())