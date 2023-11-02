def solution():
    # Calculate the total minutes of the newscast
    total_minutes = 30

    # Calculate the total minutes of news and weather
    news_and_weather_minutes = 12 + 5 + 2

    # Calculate the total minutes of advertisements
    advertisements_minutes = total_minutes - news_and_weather_minutes - 5

    result = advertisements_minutes
    return result

print(solution())