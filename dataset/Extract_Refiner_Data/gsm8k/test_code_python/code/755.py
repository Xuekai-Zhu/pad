def solution():
    
    # Define the number of songs in a playlist and the length of each song
    SONGS_PER_PLAYLIST = 300
    SONG_LENGTH = 10

    # Define the number of playlists
    NUM_PLAYLISTS = 20

    # Calculate the total length of all the songs in the playlist
    total_song_length = SONGS_PER_PLAYLIST * SONG_LENGTH * NUM_PLAYLISTS

    # Calculate the total length of all the songs in the 20 playlists
    total_length = total_song_length * NUM_PLAYLISTS

    # Display the total length of all the songs
    result = total_length
    return result

print(solution())