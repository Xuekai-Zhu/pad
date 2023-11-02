def solution():
    """Rex is taking lessons for his driver’s license. He wants to take 40 hour-long lessons before his test, and decides to have two-hour sessions twice a week until he has done his test. After 6 weeks, how many more weeks will Rex need to continue taking lessons to reach his goal?"""
    total_lessons = 40
    lessons_per_week = 2 * 2
    lessons_taken_already = 6 * lessons_per_week
    lessons_left = total_lessons - lessons_taken_already
    weeks_left = lessons_left / lessons_per_week
    result = weeks_left
    return result

print(solution())