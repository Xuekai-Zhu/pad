def solution():
    
    total_lessons = 40
    lessons_per_week = 2 * 2
    lessons_taken_already = 6 * lessons_per_week
    lessons_left = total_lessons - lessons_taken_already
    weeks_left = lessons_left / lessons_per_week
    result = weeks_left
    return result

print(solution())