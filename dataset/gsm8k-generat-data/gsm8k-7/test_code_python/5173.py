def solution():
    num_songs_side_1 = 6
    num_songs_side_2 = 4
    song_length = 4 # in minutes

    # Calculate the length of the first side of the tape
    length_side_1 = num_songs_side_1 * song_length

    # Calculate the length of the second side of the tape
    length_side_2 = num_songs_side_2 * song_length

    # Calculate the total length of the tape
    total_length = length_side_1 + length_side_2
    result = total_length
    return result

print(solution())