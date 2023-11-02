def solution():
    """A radio show plays for 3 hours a day. They split their show into talking segments, ad breaks and songs. Talking segments last 10 minutes each, ad breaks last 5 minutes each and songs are played throughout the rest of the show. If the radio show includes 3 talking segments and 5 ad breaks in today’s show, how long, in minutes, does the show play songs?"""
    
    # Define the total duration of the show in minutes
    total_duration = 3*60   # 3 hours = 3*60 minutes

    # Calculate the total duration of talking segments
    talking_duration = 3 * 10   # 3 talking segments, each lasting 10 minutes

    # Calculate the total duration of ad breaks
    ad_duration = 5 * 5   # 5 ad breaks, each lasting 5 minutes

    # Calculate the total duration of talking segments and ad breaks
    spoken_duration = talking_duration + ad_duration

    # Calculate the duration of the song segments
    song_duration = total_duration - spoken_duration

    # Return the result
    result = song_duration
    return result

print(solution())