def solution():
    vivian_songs_per_day = 10
    clara_songs_per_day = vivian_songs_per_day - 2
    num_weekends = 8
    num_weekdays = 30 - num_weekends # assuming June has 30 days

    # Calculate the total number of songs Vivian listened to
    vivian_total_songs = vivian_songs_per_day * num_weekdays

    # Calculate the total number of songs Clara listened to
    clara_total_songs = clara_songs_per_day * num_weekdays

    # Calculate the total number of songs they both listened to
    total_songs = vivian_total_songs + clara_total_songs
    result = total_songs
    return result

print(solution())