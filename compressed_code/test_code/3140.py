def solution():
    
    jenna_distance = 200
    friend_distance = 100
    jenna_speed = 50
    friend_speed = 20
    break_time = 2 * 0.5  
    jenna_drive_time = jenna_distance / jenna_speed
    friend_drive_time = friend_distance / friend_speed
    total_time = jenna_drive_time + friend_drive_time + break_time
    result = total_time
    return result

print(solution())