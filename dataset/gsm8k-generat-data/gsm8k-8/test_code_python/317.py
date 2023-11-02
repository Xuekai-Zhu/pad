def solution():
    total_hours = 7 * 24  # Total number of hours in a week
    class_hours = 18
    homework_hours_per_week = 4 * 7
    sleep_hours_per_week = 8 * 7
    work_hours_per_week = 20

    # Calculate the total hours spent on non-free time
    non_free_hours = class_hours + homework_hours_per_week + sleep_hours_per_week + work_hours_per_week

    # Calculate the remaining hours
    remaining_hours = total_hours - non_free_hours
    result = remaining_hours
    return result

print(solution())