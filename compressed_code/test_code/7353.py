def solution():
    
    songs_in_morning = 10
    songs_in_day = 15
    songs_at_night = 3
    song_size = 5 
    total_songs = songs_in_morning + songs_in_day + songs_at_night
    total_size = total_songs * song_size
    result = total_size
    return result

print(solution())