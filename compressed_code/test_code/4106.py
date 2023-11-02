def solution():
    
    total_baskets = 5
    total_tennis_balls = 15 * total_baskets
    total_soccer_balls = 5 * total_baskets
    total_initial_balls = total_tennis_balls + total_soccer_balls
    balls_removed = 3 * 8
    remaining_balls = total_initial_balls - balls_removed - 56
    balls_removed_by_other_students = remaining_balls / 2
    result = balls_removed_by_other_students
    return result

print(solution())