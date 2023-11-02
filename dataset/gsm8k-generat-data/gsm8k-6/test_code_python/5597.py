def solution():
    # Convert 4:00 PM to minutes since midnight
    time_work_ends = 16 * 60  

    # Calculate the total time spent on errands
    total_errand_time = 30 + 30 + 10 + 20  

    # Calculate the time when Jasmine starts cooking dinner
    time_jasmine_starts_cooking = time_work_ends + total_errand_time

    # Calculate the time when Jasmine finishes cooking dinner
    time_jasmine_finishes_cooking = time_jasmine_starts_cooking + 90

    # Convert the time back to a clock format
    hour = time_jasmine_finishes_cooking // 60
    minute = time_jasmine_finishes_cooking % 60
    if hour > 12:
        hour -= 12
        am_pm = "PM"
    elif hour == 12:
        am_pm = "PM"
    else:
        am_pm = "AM"

    result = f"{hour}:{minute:02d} {am_pm}"
    return result

print(solution())