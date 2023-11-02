def solution():
    """Jay went to watch a singer in a one hour 20 minutes concert. If there was a 10-minute intermission, and all the songs were 5 minutes except for one song that lasted 10 minutes, how many songs did she sing?"""
    concert_time = 80
    intermission_time = 10
    one_song_time = 5
    long_song_time = 10
    total_song_time = concert_time - intermission_time
    total_num_songs = (total_song_time - long_song_time) // one_song_time + 1
    result = total_num_songs
    return result

print(solution())