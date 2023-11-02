def solution():
    
    
    points_for_interruption = 5
    points_for_insulting = 10
    points_for_throwing = 25
    
    total_points = points_for_interruption * 2 + points_for_insulting * 4
    
    remaining_points = 100 - total_points
    
    times_can_throw = remaining_points // points_for_throwing
    
    result = times_can_throw
    
    return result

print(solution())