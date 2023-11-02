def solution():
    total_minutes = 30
    national_news_minutes = 12
    international_news_minutes = 5
    sports_minutes = 5
    weather_forecasts_minutes = 2

    # Calculate the total minutes of non-advertisement content
    non_ad_minutes = national_news_minutes + international_news_minutes + sports_minutes + weather_forecasts_minutes

    # Subtract the non-advertisement minutes from the total minutes to get the advertising minutes
    advertising_minutes = total_minutes - non_ad_minutes
    result = advertising_minutes
    return result

print(solution())