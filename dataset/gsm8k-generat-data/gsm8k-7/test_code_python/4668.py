def solution():
    weekday_homework = 2 * 5  # 2 hours per night for 5 weekdays
    weekend_homework = 5  # 5 hours for the entire weekend
    total_homework = weekday_homework + weekend_homework

    nights_available = 5 - 2  # 5 weekdays minus 2 nights for practice
    hours_needed_per_night = total_homework / nights_available

    result = hours_needed_per_night
    return result

print(solution())