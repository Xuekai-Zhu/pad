def solution():
    """A radio show plays for 3 hours a day. They split their show into talking segments, ad breaks and songs. Talking segments last 10 minutes each, ad breaks last 5 minutes each and songs are played throughout the rest of the show. If the radio show includes 3 talking segments and 5 ad breaks in today’s show, how long, in minutes, does the show play songs?"""
    # Define the length of each talking segment and ad break in minutes
    TALKING_LENGTH = 10
    AD_BREAK_LENGTH = 5

    # Calculate the total length of talking segments and ad breaks
    total_length = (3 * 60) - (3 * TALKING_LENGTH) - (5 * AD_BREAK_LENGTH)

    # The rest of the time is spent playing songs
    song_length = total_length

    # Display the length of time the show plays songs
    result = song_length
    return result

print(solution())