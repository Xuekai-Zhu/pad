def solution():
    
    distance_to_school = 7
    days_without_friday = 4
    distance_from_school_to_friend = 2
    total_distance_without_friday = distance_to_school * days_without_friday * 2  
    total_distance_on_friday = distance_to_school * 2 + distance_from_school_to_friend * 2 
    total_distance = total_distance_without_friday + total_distance_on_friday
    result = total_distance
    return result

print(solution())