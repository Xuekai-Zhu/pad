def solution():
    # Calculate the total number of hours Madeline spends on homework and sleeping each week
    homework_time = 4 * 7  # Madeline works on homework 4 hours per day, for 7 days a week
    sleep_time = 8 * 7  # Madeline sleeps 8 hours per day, for 7 days a week
    total_nonclass_time = homework_time + sleep_time  # total non-class time per week

    # Calculate the total number of hours Madeline has left over after subtracting class time and work hours
    total_time = 168  # total hours in a week
    class_time = 18  # Madeline spends 18 hours per week in class
    work_time = 20  # Madeline works part-time for 20 hours per week
    remaining_time = total_time - class_time - work_time - total_nonclass_time
    result = remaining_time
    return result

print(solution())