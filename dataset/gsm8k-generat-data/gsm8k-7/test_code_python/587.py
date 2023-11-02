def solution():
    weekend_catch_up = 3 * (3 * 2)  # Three times as many hours on the weekend catching up as working
    weekday_work = 4 * (3 * 4)  # Four times as many hours working on weekdays as catching up
    total_working_hours = weekend_catch_up + weekday_work
    result = total_working_hours
    return result

print(solution())