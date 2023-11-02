def solution():
    soccer_balls = 40
    basketballs = 15
    soccer_balls_with_holes = 30
    basketballs_with_holes = 7
    total_balls_without_holes = soccer_balls + basketballs - soccer_balls_with_holes - basketballs_with_holes
    result = total_balls_without_holes
    return result

print(solution())