def solution():
    articles_per_30_mins = 5
    work_hours_per_day = 4
    work_days_per_week = 5

    # Calculate the total number of articles Helga can write in a week
    total_articles_per_week = (articles_per_30_mins * 2) * (work_hours_per_day * work_days_per_week)

    # Calculate the total number of articles Helga wrote last Thursday and Friday
    extra_hours = [2, 3]
    extra_articles = []
    for hours in extra_hours:
        articles = (articles_per_30_mins * 2) * (hours / 0.5)
        extra_articles.append(articles)

    # Calculate the total number of articles Helga wrote this week
    total_articles_this_week = total_articles_per_week + sum(extra_articles)
    result = total_articles_this_week
    return result

print(solution())