def solution():
    monday_lessons = 6
    monday_lesson_duration = 0.5  # 30 minutes is half an hour
    tuesday_lessons = 3
    tuesday_lesson_duration = 1  # 1 hour
    wednesday_lesson_duration = 2 * tuesday_lesson_duration
    total_hours = (monday_lessons * monday_lesson_duration) + (tuesday_lessons * tuesday_lesson_duration) + wednesday_lesson_duration
    result = total_hours
    return result

print(solution())