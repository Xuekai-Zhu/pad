def solution():
    initial_songs = 500
    songs_added_1 = 500
    songs_added_2 = initial_songs + songs_added_1
    songs_added_3 = songs_added_2 * 2
    songs_removed = 50
    final_songs = songs_added_3 - songs_removed
    result = final_songs
    return result

print(solution())