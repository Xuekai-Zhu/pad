def solution():
    # Calculate the distance driven in the first 5 hours
    distance_first_5_hrs = 8 * 5 

    # Calculate the total time spent driving and cooling down 
    total_time = 13  

    # Calculate the distance driven in the remaining 8 hours
    distance_remaining_8_hrs = 8 * 8  

    # Calculate the total distance driven in 13 hours
    total_distance = distance_first_5_hrs + distance_remaining_8_hrs 

    result = total_distance
    return result

print(solution())