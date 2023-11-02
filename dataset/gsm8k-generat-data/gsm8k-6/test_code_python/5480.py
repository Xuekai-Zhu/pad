def solution():
    # Calculate the total hours Helga worked this week
    total_hours = (4*5) + 2 + 3  # Helga usually works 4 hours a day for 5 days a week, and worked an extra 2 hours on Thursday and 3 hours on Friday

    # Calculate the total number of articles Helga can write in one hour
    articles_per_hour = 5 / 0.5  # Helga can write 5 articles in 30 minutes

    # Calculate the total number of articles Helga wrote this week
    total_articles = articles_per_hour * total_hours

    result = total_articles
    return result

print(solution())