def solution():
    """Out of the 150 teachers on the school basketball court, 60% are history teachers. If the rest of the teachers on the court are math teachers, and each teacher sleeps for 6 hours a day, calculate the total time the math teachers collectively spend sleeping in one day."""
    total_teachers = 150
    history_teachers = 0.6 * total_teachers
    math_teachers = total_teachers - history_teachers
    total_sleep_time = math_teachers * 6
    result = total_sleep_time
    return result

print(solution())