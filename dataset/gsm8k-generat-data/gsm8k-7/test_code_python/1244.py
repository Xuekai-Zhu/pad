def solution():
    songs_per_month = 3
    hours_per_day = 10
    days_to_complete_song = 10

    # Calculate the total number of hours needed to complete one song
    total_hours_per_song = hours_per_day * days_to_complete_song

    # Calculate the total number of hours needed to complete all three songs
    total_hours = total_hours_per_song * songs_per_month
    result = total_hours
    return result

print(solution())