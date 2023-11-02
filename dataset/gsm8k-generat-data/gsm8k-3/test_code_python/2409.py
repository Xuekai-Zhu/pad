def solution():
    """Vivian plays 10 Spotify songs every day. Her best friend Clara plays 2 fewer songs each day. If in June they didn't play any song during the weekends only, and there were 8 weekend days in June, what's the total number of songs they both listened to in that month?"""

    # Define the number of songs Vivian plays each day
    vivian_songs = 10

    # Define the number of songs Clara plays each day
    clara_songs = vivian_songs - 2

    # Calculate the total number of songs they both listen to on weekdays
    weekday_songs = (vivian_songs + clara_songs) * 5 * 4

    # Calculate the total number of songs they both listen to on weekends
    weekend_songs = 0

    # There are 8 weekend days in June
    weekend_songs = (vivian_songs + clara_songs) * 2 * 8

    # Calculate the total number of songs they both listen to in June
    total_songs = weekday_songs + weekend_songs

    # Display the total number of songs
    result = total_songs
    return result

print(solution())