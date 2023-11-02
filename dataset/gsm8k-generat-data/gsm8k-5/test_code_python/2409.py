def solution():
    songs_per_day = 10  # Vivian plays 10 songs per day
    clara_songs_per_day = songs_per_day - 2  # Clara plays 2 fewer songs per day
    total_weekend_days = 8  # There are 8 weekend days in June

    # Calculate the total number of songs Vivian played in June
    vivian_june_songs = songs_per_day * (30 - total_weekend_days)

    # Calculate the total number of songs Clara played in June
    clara_june_songs = clara_songs_per_day * (30 - total_weekend_days)

    # Calculate the total number of songs they both listened to
    total_songs = vivian_june_songs + clara_june_songs
    result = total_songs
    return result

print(solution())