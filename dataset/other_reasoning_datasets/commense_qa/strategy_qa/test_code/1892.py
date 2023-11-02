def solution():
    # Define the number of songs, song length, and minutes in a year
    num_songs = 43000000
    song_length = 3
    minutes_in_year = 525600
    # Calculate the total minutes of all songs
    total_minutes = num_songs * song_length
    if total_minutes <= minutes_in_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())