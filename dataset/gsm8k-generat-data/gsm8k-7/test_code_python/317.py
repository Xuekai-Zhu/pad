def solution():
    hours_per_day = 24
    class_hours_per_week = 18
    homework_hours_per_day = 4
    sleep_hours_per_day = 8
    work_hours_per_week = 20

    # Calculate the total number of hours Madeline spends on sleep each week
    total_sleep_hours = sleep_hours_per_day * 7

    # Calculate the total number of hours Madeline spends on homework each week
    total_homework_hours = homework_hours_per_day * 7

    # Calculate the total number of work hours Madeline has each week
    total_work_hours = work_hours_per_week

    # Calculate the total number of hours Madeline has left over each week
    total_leftover_hours = hours_per_day * 7 - (class_hours_per_week + total_homework_hours + total_sleep_hours + total_work_hours)
    result = total_leftover_hours
    return result

print(solution())