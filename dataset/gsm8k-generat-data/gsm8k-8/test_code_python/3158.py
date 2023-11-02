def solution():
    total_lessons = 40
    lessons_per_week = 2 * 2 # 2-hour sessions, twice a week
    weeks_passed = 6
    total_lessons_taken = lessons_per_week * weeks_passed
    lessons_left = total_lessons - total_lessons_taken
    additional_weeks_needed = lessons_left // lessons_per_week

    result = additional_weeks_needed
    return result

print(solution())