def solution():
    total_lessons = 40
    lessons_per_week = 2 * 2  # two 2-hour sessions per week
    weeks_so_far = 6

    # Calculate the total number of lessons that Rex has taken so far
    total_lessons_so_far = weeks_so_far * lessons_per_week

    # Calculate the number of lessons that Rex still needs
    remaining_lessons = total_lessons - total_lessons_so_far

    # Calculate the number of weeks that Rex still needs to continue taking lessons
    remaining_weeks = remaining_lessons / lessons_per_week
    result = remaining_weeks
    return result

print(solution())