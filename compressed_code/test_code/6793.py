def solution():
    
    susan_speed = 1
    pete_backward_speed = 3 * susan_speed
    tracy_speed = 2 * susan_speed
    pete_hand_speed = 0.25 * tracy_speed
    pete_hand_speed_mph = 2
    pete_backward_speed_mph = pete_backward_speed * susan_speed * pete_hand_speed_mph / pete_hand_speed
    result = pete_backward_speed_mph
    return result

print(solution())