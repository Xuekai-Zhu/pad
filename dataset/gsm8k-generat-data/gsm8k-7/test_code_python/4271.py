def solution():
    time_to_hidden_lake = 15
    time_back_to_park_office = 7
    total_time_away = 32
    
    # Calculate the time spent walking to and from Hidden Lake
    total_walk_time = time_to_hidden_lake + time_back_to_park_office
    
    # Calculate the time spent at Hidden Lake
    time_at_hidden_lake = total_time_away - total_walk_time
    
    # Calculate the total time spent walking
    total_walk_time = time_to_hidden_lake + time_at_hidden_lake
    
    # Calculate the time spent walking from the Park Office to the Lake Park restaurant
    walk_time_to_restaurant = total_walk_time - time_to_hidden_lake
    
    result = walk_time_to_restaurant
    return result

print(solution())