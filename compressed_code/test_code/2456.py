def solution():
    
    lessons_goal = 40
    lessons_per_week = 2 * 2  
    weeks_completed = 6
    hours_completed = weeks_completed * lessons_per_week
    hours_remaining = lessons_goal - hours_completed
    weeks_remaining = hours_remaining / lessons_per_week
    result = weeks_remaining
    return result

print(solution())