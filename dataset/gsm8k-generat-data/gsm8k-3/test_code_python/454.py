def solution():
    """The half-hour newscast includes 12 minutes of national news, 5 minutes of international news, 5 minutes of sports, and 2 minutes of weather forecasts. The rest is advertisements. How many minutes of advertising are in the newscast?"""
    # Define the total length of the newscast
    NEWSCAST_LENGTH = 30

    # Define the length of each segment of the newscast
    NATIONAL_NEWS_LENGTH = 12
    INTERNATIONAL_NEWS_LENGTH = 5
    SPORTS_LENGTH = 5
    WEATHER_LENGTH = 2

    # Calculate the total length of the non-advertising segments
    non_advertising_length = NATIONAL_NEWS_LENGTH + INTERNATIONAL_NEWS_LENGTH + SPORTS_LENGTH + WEATHER_LENGTH

    # Calculate the length of the advertising segment
    advertising_length = NEWSCAST_LENGTH - non_advertising_length

    # Display the length of the advertising segment
    result = advertising_length
    return result

print(solution())