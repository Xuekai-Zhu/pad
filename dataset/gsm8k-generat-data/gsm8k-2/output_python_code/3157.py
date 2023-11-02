def solution():
    """Rex is taking lessons for his driver’s license. He wants to take 40 hour-long lessons before his test, and decides to have two-hour sessions twice a week until he has done his test. After 6 weeks, how many more weeks will Rex need to continue taking lessons to reach his goal?"""
    lessons_goal = 40
    lessons_per_week = 2 * 2  # two-hour sessions twice a week
    weeks_completed = 6
    hours_completed = weeks_completed * lessons_per_week
    hours_remaining = lessons_goal - hours_completed
    weeks_remaining = hours_remaining / lessons_per_week
    result = weeks_remaining
    return result

print(solution())