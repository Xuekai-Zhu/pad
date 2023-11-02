def solution():
    """Minnie is making a playlist of songs for a party she will be throwing. She wants the playlist to be an hour long. She has added 16 three-minute songs to the playlist. How many four-minute songs does she have to add to make sure the playlist is an hour long?"""
    total_time_in_minutes = 60
    songs_added = 16
    minutes_of_added_songs = songs_added * 3
    minutes_left = total_time_in_minutes - minutes_of_added_songs
    minutes_per_four_minute_song = 4
    songs_needed = minutes_left // minutes_per_four_minute_song
    result = songs_needed
    return result

print(solution())