def solution():
    total_hours = 168  # There are 24 hours in a day, so 7 days a week totals 168 hours
    class_hours = 18  # Madeline spends 18 hours per week in class
    homework_hours = 4 * 7  # Madeline spends 4 hours each day on homework, so total 28 hours per week
    sleep_hours = 8 * 7  # Madeline sleeps 8 hours each day, so total 56 hours per week
    work_hours = 20  # Madeline works part-time 20 hours per week

    # Calculate the total hours Madeline spends on school, homework, sleep, and work
    total_spent_hours = class_hours + homework_hours + sleep_hours + work_hours

    # Calculate the hours left over
    hours_left_over = total_hours - total_spent_hours
    result = hours_left_over
    return result

print(solution())