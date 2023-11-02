def solution():
    initial_songs = 500
    songs_added_week1 = 500
    double_initial_songs = 2 * initial_songs
    songs_removed = 50

    # Calculate the total number of songs on Aisha's mp3 player after adding and removing songs
    total_songs = initial_songs + songs_added_week1 + double_initial_songs - songs_removed
    result = total_songs
    return result

print(solution())