def solution():
    total_lessons = 40
    lessons_per_week = 2 # two-hour sessions twice a week
    weeks_so_far = 6
    lessons_so_far = lessons_per_week * weeks_so_far

    # Calculate how many more lessons Rex needs to take
    lessons_remaining = total_lessons - lessons_so_far

    # Calculate how many more weeks Rex needs to continue taking lessons
    weeks_remaining = lessons_remaining / lessons_per_week

    result = weeks_remaining
    return result

print(solution())