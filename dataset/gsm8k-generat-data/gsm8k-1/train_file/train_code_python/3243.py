def solution():
    """A radio show plays for 3 hours a day. They split their show into talking segments, ad breaks and songs. Talking segments last 10 minutes each, ad breaks last 5 minutes each and songs are played throughout the rest of the show. If the radio show includes 3 talking segments and 5 ad breaks in today’s show, how long, in minutes, does the show play songs?"""
    total_time = 180 # in minutes
    talking_segments = 3
    ad_breaks = 5
    talking_time = talking_segments * 10 # in minutes
    ad_break_time = ad_breaks * 5 # in minutes
    total_time_spent = talking_time + ad_break_time # in minutes
    song_time = total_time - total_time_spent # in minutes
    result = song_time
    return result

print(solution())