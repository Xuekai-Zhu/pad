def solution():
    song1_length = 3
    song2_length = 2
    song3_length = 3
    playlist_length = song1_length + song2_length + song3_length

    ride_length = 40

    # Calculate the number of times Gabe can listen to his playlist
    num_plays = ride_length // playlist_length
    result = num_plays
    return result

print(solution())