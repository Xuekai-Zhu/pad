def solution():
    num_3min_songs = 16
    length_of_3min_song = 3   # in minutes
    length_of_4min_song = 4   # in minutes
    total_playlist_length = 60   # in minutes

    # Calculate the total length of the 3-minute songs
    total_3min_songs_length = num_3min_songs * length_of_3min_song

    # Calculate the remaining length needed for the playlist to be an hour long
    remaining_length = total_playlist_length - total_3min_songs_length

    # Calculate the number of 4-minute songs needed to fill up the remaining length
    num_4min_songs = remaining_length / length_of_4min_song
    result = num_4min_songs
    return result

print(solution())