def solution():
    """Gabe has three songs on his playlist. “The Best Day” is 3 minutes, “Raise the Roof” is 2 minutes, and “Rap Battle” is 3 minutes. How many times can Gabe listen to his entire playlist on the 40-minute ride to his wrestling match?"""
    # Define the duration of each song and the total duration of the playlist
    song1_duration = 3
    song2_duration = 2
    song3_duration = 3
    playlist_duration = song1_duration + song2_duration + song3_duration

    # Calculate the number of times the playlist can be listened to during the 40-minute ride
    num_playlists = 40 // playlist_duration

    # return the result
    result = num_playlists
    return result

print(solution())