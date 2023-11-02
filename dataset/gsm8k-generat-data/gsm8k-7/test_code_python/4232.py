def solution():
    num_singles = 5
    num_albums_15_songs = 2
    num_songs_15_songs_album = 15
    num_songs_20_songs_album = 20

    # Calculate the total number of songs in the 2 albums with 15 songs each
    total_songs_15_songs_albums = num_albums_15_songs * num_songs_15_songs_album

    # Calculate the total number of songs in the album with 20 songs
    total_songs_20_songs_album = num_songs_20_songs_album

    # Calculate the total number of songs released by Beyonce
    total_songs_released = num_singles + total_songs_15_songs_albums + total_songs_20_songs_album
    result = total_songs_released
    return result

print(solution())