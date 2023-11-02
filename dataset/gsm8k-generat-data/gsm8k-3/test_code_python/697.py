def solution():
    """Joey studies for his SAT exams 2 hours per night 5 nights a week.  On the weekends, he studies 3 hours a day.  If his SAT exam is 6 weeks away, how much time will Joey spend studying?"""
    # Calculate the total number of hours spent studying on weekdays
    weekday_hours = 2 * 5 * 6

    # Calculate the total number of hours spent studying on weekends
    weekend_hours = 3 * 2 * 6

    # Calculate the total number of hours Joey spends studying
    total_hours = weekday_hours + weekend_hours

    # Display the total number of hours Joey spends studying
    result = total_hours
    return result

print(solution())