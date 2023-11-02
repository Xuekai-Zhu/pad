def solution():
    Grayson_motorboat_speed1 = 25
    Grayson_motorboat_speed2 = 20
    Grayson_motorboat_time1 = 1
    Grayson_motorboat_time2 = 0.5
    Rudy_rowboat_speed = 10
    Rudy_rowboat_time = 3
    Grayson_motorboat_distance1 = Grayson_motorboat_speed1 * Grayson_motorboat_time1
    Grayson_motorboat_distance2 = Grayson_motorboat_speed2 * Grayson_motorboat_time2
    Rudy_rowboat_distance = Rudy_rowboat_speed * Rudy_rowboat_time
    Grayson_total_distance = Grayson_motorboat_distance1 + Grayson_motorboat_distance2
    difference_in_distance = Grayson_total_distance - Rudy_rowboat_distance
    result = difference_in_distance
    
    return result

print(solution())