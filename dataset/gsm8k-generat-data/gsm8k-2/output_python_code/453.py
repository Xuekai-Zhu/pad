def solution():
    """The half-hour newscast includes 12 minutes of national news, 5 minutes of international news, 5 minutes of sports, and 2 minutes of weather forecasts. The rest is advertisements. How many minutes of advertising are in the newscast?"""
    total_time = 30
    news_time = 12 + 5 + 5 + 2
    ad_time = total_time - news_time
    result = ad_time
    return result

print(solution())