def solution():
    # Calculate the total length of newscast
    total_length = 30  # half-hour newscast

    # Calculate the total length of news segments
    news_length = 12 + 5 + 5 + 2  # 12 minutes of national news, 5 minutes of international news, 5 minutes of sports, and 2 minutes of weather forecasts

    # Calculate the length of advertising
    ad_length = total_length - news_length
    result = ad_length
    return result

print(solution())