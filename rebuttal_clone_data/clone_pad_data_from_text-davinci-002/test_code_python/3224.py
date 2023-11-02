def solution():
   trip_time = 15
    speed_1 = 16
    speed_2 = 12
    speed_3 = 20
    distance_1 = speed_1 * (trip_time / 60)
    distance_2 = speed_2 * (trip_time / 60)
    distance_3 = speed_3 * (trip_time / 60)
    total_distance = distance_1 + distance_2 + distance_3
 
    result = total_distance
    return result

print(solution())