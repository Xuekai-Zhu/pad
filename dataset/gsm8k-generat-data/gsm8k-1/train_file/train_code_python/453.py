def solution():
    """The half-hour newscast includes 12 minutes of national news, 5 minutes of international news, 5 minutes of sports, and 2 minutes of weather forecasts. The rest is advertisements. How many minutes of advertising are in the newscast?"""
    total_minutes = 30
    news_minutes = 12 + 5 + 5 + 2
    advertising_minutes = total_minutes - news_minutes
    result = advertising_minutes
    return result

print(solution())