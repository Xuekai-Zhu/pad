def solution():
    """John buys 20 hours of music a month. The average length of a song is 3 minutes. He buys each song for $.50. How much does he pay for music a year?"""
    hours_per_month = 20
    minutes_per_hour = 60
    minutes_per_month = hours_per_month * minutes_per_hour
    songs_per_month = minutes_per_month / 3
    cost_per_song = 0.5
    cost_per_month = songs_per_month * cost_per_song
    cost_per_year = cost_per_month * 12
    result = cost_per_year
    return result

print(solution())