def solution():
    articles_per_30_minutes = 5  # Helga can write 5 articles every 30 minutes
    minutes_per_hour = 60  # There are 60 minutes in an hour
    hours_per_day = 4  # Helga usually works 4 hours a day
    days_per_week = 5  # Helga works 5 days a week
    extra_hours_last_thursday = 2  # Helga worked 2 extra hours last Thursday
    extra_hours_last_friday = 3  # Helga worked 3 extra hours last Friday

    # Calculate the total number of articles Helga can write in a regular week
    articles_regular_week = articles_per_30_minutes * (minutes_per_hour / 30) * hours_per_day * days_per_week

    # Calculate the total number of articles Helga wrote last Thursday and Friday
    articles_extra = articles_per_30_minutes * (minutes_per_hour / 30) * (extra_hours_last_thursday + extra_hours_last_friday)

    # Calculate the total number of articles Helga wrote this week
    articles_this_week = articles_regular_week + articles_extra
    result = articles_this_week
    return result

print(solution())