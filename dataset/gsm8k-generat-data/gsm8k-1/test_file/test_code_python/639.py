def solution():
    """A news website publishes an average of 20 political and weather news articles every day. Its sister company publishes an average of 10 business news articles daily. Calculate the total number of articles the two websites published together in February if there are 28 days in the month."""
    political_and_weather_articles_per_day = 20
    business_articles_per_day = 10
    days_in_february = 28
    total_articles = (political_and_weather_articles_per_day + business_articles_per_day) * days_in_february
    result = total_articles
    return result

print(solution())