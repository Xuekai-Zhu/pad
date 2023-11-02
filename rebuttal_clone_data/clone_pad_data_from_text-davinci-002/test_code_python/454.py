def solution():
    national_news = 12
    international_news = 5
    sports = 5
    weather = 2
    total_news = national_news + international_news + sports + weather
    total_time = 30
    advertisements = total_time - total_news
    result = advertisements
    return result

print(solution())