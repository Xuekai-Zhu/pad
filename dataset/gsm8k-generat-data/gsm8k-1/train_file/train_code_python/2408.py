def solution():
    """Vivian plays 10 Spotify songs every day. Her best friend Clara plays 2 fewer songs each day. If in June they didn't play any song during the weekends only, and there were 8 weekend days in June, what's the total number of songs they both listened to in that month?"""
    songs_per_day_vivian = 10
    songs_per_day_clara = songs_per_day_vivian - 2
    days_in_june = 30
    weekend_days_in_june = 8
    total_days_june = days_in_june - weekend_days_in_june
    total_songs_vivian = songs_per_day_vivian * total_days_june
    total_songs_clara = songs_per_day_clara * total_days_june
    total_songs_both = total_songs_vivian + total_songs_clara
    result = total_songs_both
    return result

print(solution())