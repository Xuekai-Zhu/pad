def solution():
    """Jay went to watch a singer in a one hour 20 minutes concert. If there was a 10-minute intermission, and all the songs were 5 minutes except for one song that lasted 10 minutes, how many songs did she sing?"""
    concert_time = 80  # in minutes
    intermission_time = 10  # in minutes
    song_time = 5  # in minutes (except for one song)
    long_song_time = 10  # in minutes (for one song)
    
    # Calculate total time spent on songs
    total_song_time = concert_time - intermission_time
    # Subtract duration of long song from total song time
    total_song_time -= long_song_time
    # Calculate number of regular-length songs
    num_songs = total_song_time // song_time
    
    # Add 1 for the long song
    num_songs += 1
    
    result = num_songs
    return result

print(solution())