def solution():
    """Joey studies for his SAT exams 2 hours per night 5 nights a week. On the weekends, he studies 3 hours a day. If his SAT exam is 6 weeks away, how much time will Joey spend studying?"""
    # Define the number of nights Joey studies per week
    study_nights_per_week = 5

    # Define the number of hours Joey studies per night
    study_hours_per_night = 2

    # Define the number of hours Joey studies per day on weekends
    study_hours_weekend = 3

    # Define the total number of weeks before the exam
    total_weeks = 6

    # Calculate the total number of hours Joey will study during the weekdays
    weekday_hours = study_nights_per_week * study_hours_per_night

    # Calculate the total number of hours Joey will study during the weekends
    weekend_hours = 2 * study_hours_weekend

    # Calculate the total number of hours Joey will study during the entire 6 weeks
    total_hours = weekday_hours * total_weeks + weekend_hours * 6

    # return the result
    result = total_hours
    return result

print(solution())