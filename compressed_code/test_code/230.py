def solution():
    
    goal_pages_per_week = 7 * 50
    total_pages_read = 43 + 65 + 28 + 0 + 70 + 56
    pages_left_to_read = goal_pages_per_week - total_pages_read
    result = pages_left_to_read
    return result

print(solution())