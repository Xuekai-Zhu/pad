def solution():
    
    first_side_songs = 6
    second_side_songs = 4
    song_length = 4
    first_side_length = first_side_songs * song_length
    second_side_length = second_side_songs * song_length
    total_tape_length = first_side_length + second_side_length
    result = total_tape_length
    return result

print(solution())