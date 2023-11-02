def solution():
    """Vivian plays 10 Spotify songs every day. Her best friend Clara plays 2 fewer songs each day. If in June they didn't play any song during the weekends only, and there were 8 weekend days in June, what's the total number of songs they both listened to in that month?"""
    # Define the number of songs Vivian plays each day and the number of songs Clara plays each day
    vivian_songs = 10
    clara_songs = vivian_songs - 2

    # Define the number of weekend days in June
    weekend_days = 8

    # Calculate the total number of songs Vivian plays in June (excluding weekends)
    vivian_total_songs = (30 - weekend_days) * vivian_songs

    # Calculate the total number of songs Clara plays in June (excluding weekends)
    clara_total_songs = (30 - weekend_days) * clara_songs

    # Calculate the total number of songs they both listened to in June
    total_songs = vivian_total_songs + clara_total_songs

    # return the result
    result = total_songs
    return result

print(solution())