def solution():
    # Calculate the total duration of talking segments and ad breaks
    total_talking_duration = 3 * 10  # the radio show has 3 talking segments, each lasting 10 minutes
    total_ad_duration = 5 * 5  # the radio show has 5 ad breaks, each lasting 5 minutes
    total_talking_and_ad_duration = total_talking_duration + total_ad_duration

    # Calculate the total duration of the show
    total_duration = 3 * 60  # the radio show plays for 3 hours, which is 180 minutes

    # Calculate the duration of the songs played
    duration_of_songs = total_duration - total_talking_and_ad_duration
    result = duration_of_songs
    return result

print(solution())