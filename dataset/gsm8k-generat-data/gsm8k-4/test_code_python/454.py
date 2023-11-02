def solution():
    """The half-hour newscast includes 12 minutes of national news, 5 minutes of international news, 5 minutes of sports, and 2 minutes of weather forecasts. The rest is advertisements. How many minutes of advertising are in the newscast?"""
    # Define the total length of the newscast
    total_length = 30

    # Calculate the total length of news segments
    news_length = 12 + 5 + 5 + 2

    # Calculate the length of advertisements
    ad_length = total_length - news_length

    # return the result
    result = ad_length
    return result

print(solution())