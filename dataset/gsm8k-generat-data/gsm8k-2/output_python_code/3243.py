def solution():
    """A radio show plays for 3 hours a day. They split their show into talking segments, ad breaks and songs. Talking segments last 10 minutes each, ad breaks last 5 minutes each and songs are played throughout the rest of the show. If the radio show includes 3 talking segments and 5 ad breaks in today’s show, how long, in minutes, does the show play songs?"""
    total_time = 3 * 60 # convert to minutes
    talking_segments = 3 * 10 # minutes
    ad_breaks = 5 * 5 # minutes
    used_time = talking_segments + ad_breaks
    song_time = total_time - used_time
    result = song_time
    return result

print(solution())