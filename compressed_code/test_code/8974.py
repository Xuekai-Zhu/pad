def solution():
    
    jenna_distance = 200
    friend_distance = 100
    jenna_speed = 50
    friend_speed = 20
    total_distance = jenna_distance + friend_distance
    time_driving = (jenna_distance / jenna_speed) + (friend_distance / friend_speed)
    time_breaks = 2 * 0.5 
    total_time = time_driving + time_breaks
    result = total_time
    return result

print(solution())