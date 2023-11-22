def solution():
    
    # Define the number of days in February
    DAYS_IN_FEBRUARY = 28

    # Define the number of articles published by each website per day
    political_articles = 20
    weather_articles = 20
    business_articles = 10

    # Calculate the total number of articles published by each website in February
    total_political_articles = political_articles * DAYS_IN_FEBRUARY
    total_weather_articles = weather_articles * DAYS_IN_FEBRUARY
    total_business_articles = business_articles * DAYS_IN_FEBRUARY

    # Calculate the total number of articles published by both websites in February
    total_articles = total_political_articles + total_weather_articles + total_business_articles

    # Display the total number of articles published
    result = total_articles
    return result

print(solution())