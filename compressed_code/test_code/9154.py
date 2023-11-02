def solution():
    
    total_time = 32
    to_lake_time = 15
    back_to_office_time = 7
    walking_time_to_lake_restaurant = total_time - to_lake_time - back_to_office_time
    result = walking_time_to_lake_restaurant
    return result

print(solution())