def solution():
    
    songs_in_repertoire = 30
    first_set_songs = 5
    second_set_songs = 7
    encore_songs = 2
    total_songs_played = first_set_songs + second_set_songs + encore_songs
    songs_left = songs_in_repertoire - total_songs_played
    avg_songs_third_fourth = songs_left / 2
    result = avg_songs_third_fourth
    return result

print(solution())