def solution():
    # Calculate the total minutes Helga works in a week
    total_minutes = 4 * 60 * 5 + 2 * 60 + 3 * 60

    # Calculate the total articles Helga can write in a minute
    articles_per_minute = 5 / 30

    # Calculate the total articles Helga can write in a week
    total_articles = total_minutes * articles_per_minute

    result = total_articles
    return result

print(solution())