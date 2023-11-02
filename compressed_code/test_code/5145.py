def solution():
    
    horse_speed = 20
    bullet_speed = 400
    relative_speed_same_direction = bullet_speed - horse_speed
    relative_speed_opposite_direction = bullet_speed + horse_speed
    speed_difference = relative_speed_same_direction - relative_speed_opposite_direction
    result = abs(speed_difference)
    return result

print(solution())