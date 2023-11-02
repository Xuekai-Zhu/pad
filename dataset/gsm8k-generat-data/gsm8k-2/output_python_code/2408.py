def solution():
    """Vivian plays 10 Spotify songs every day. Her best friend Clara plays 2 fewer songs each day. If in June they didn't play any song during the weekends only, and there were 8 weekend days in June, what's the total number of songs they both listened to in that month?"""
    vivian_songs = 10
    clara_songs = vivian_songs - 2
    weekdays_in_june = 30 - 8
    vivian_total_songs = vivian_songs * weekdays_in_june
    clara_total_songs = clara_songs * weekdays_in_june
    total_songs = vivian_total_songs + clara_total_songs
    result = total_songs
    return result

print(solution())