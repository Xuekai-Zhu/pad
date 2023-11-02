def solution():
    """Minnie is making a playlist of songs for a party she will be throwing. She wants the playlist to be an hour long. She has added 16 three-minute songs to the playlist. How many four-minute songs does she have to add to make sure the playlist is an hour long?"""
    total_time = 60
    added_time = 16 * 3
    remaining_time = total_time - added_time
    songs_needed = remaining_time // 4
    result = songs_needed
    return result

print(solution())