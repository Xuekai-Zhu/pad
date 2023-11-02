def solution():
    hours_per_weekday = 2  # Joey studies for 2 hours per night on weekdays
    days_per_weekday = 5  # Joey studies for 5 days on weekdays
    hours_per_weekend_day = 3  # Joey studies for 3 hours per day on weekends
    days_per_weekend = 2  # Joey studies for 2 days on weekends
    weeks = 6  # Joey has 6 weeks until his SAT exam

    # Calculate the total hours Joey will spend studying on weekdays
    total_weekday_hours = hours_per_weekday * days_per_weekday * weeks

    # Calculate the total hours Joey will spend studying on weekends
    total_weekend_hours = hours_per_weekend_day * days_per_weekend * weeks

    # Calculate the total time Joey will spend studying
    total_study_time = total_weekday_hours + total_weekend_hours
    result = total_study_time
    return result

print(solution())