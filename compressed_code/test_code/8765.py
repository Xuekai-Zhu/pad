def solution():
    
    total_soccer_balls = 40
    total_basketballs = 15
    soccer_balls_with_holes = 30
    basketballs_with_holes = 7
    soccer_balls_without_holes = total_soccer_balls - soccer_balls_with_holes
    basketballs_without_holes = total_basketballs - basketballs_with_holes
    total_balls_without_holes = soccer_balls_without_holes + basketballs_without_holes
    result = total_balls_without_holes
    return result

print(solution())