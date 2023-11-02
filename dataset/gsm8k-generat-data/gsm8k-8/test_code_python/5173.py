def solution():
    # Define the number of songs on each side and the length of each song
    songs_side1 = 6
    songs_side2 = 4
    song_length = 4

    # Calculate the total length of the tape
    total_length = (songs_side1 + songs_side2) * song_length
    result = total_length
    return result

print(solution())