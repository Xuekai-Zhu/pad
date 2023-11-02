def solution():
    """Helga works for a newspaper company. She can write 5 articles every 30 minutes, and she usually works 4 hours a day 5 days a week. If Helga worked an extra 2 hours last Thursday, and an extra 3 hours last Friday, how many articles was she able to write this week?"""
    # Define the number of articles Helga can write in 30 minutes
    ARTICLES_PER_30MIN = 5

    # Define the number of hours Helga usually works per day
    HOURS_PER_DAY = 4

    # Define the number of days Helga usually works per week
    DAYS_PER_WEEK = 5

    # Define the extra hours Helga worked on Thursday and Friday
    EXTRA_HOURS_THU = 2
    EXTRA_HOURS_FRI = 3

    # Calculate the total number of hours Helga worked this week
    total_hours = (HOURS_PER_DAY * DAYS_PER_WEEK) + EXTRA_HOURS_THU + EXTRA_HOURS_FRI

    # Calculate the total number of articles Helga wrote this week
    total_articles = (total_hours * 2) * ARTICLES_PER_30MIN

    result = total_articles
    return result

print(solution())