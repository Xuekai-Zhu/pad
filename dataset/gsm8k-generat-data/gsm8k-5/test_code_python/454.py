def solution():
    total_minutes = 30  # The newscast is 30 minutes long
    news_minutes = 12 + 5  # The national and international news segments take up 12 and 5 minutes respectively
    sports_minutes = 5  # The sports segment takes up 5 minutes
    weather_minutes = 2  # The weather forecast takes up 2 minutes

    # Calculate the total minutes of advertising by subtracting the time taken by the news, sports, and weather segments
    advertising_minutes = total_minutes - news_minutes - sports_minutes - weather_minutes
    result = advertising_minutes
    return result

print(solution())