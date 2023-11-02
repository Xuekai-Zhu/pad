def solution():
    num_songs = 10
    song_length = 3.5  # minutes
    jump_rate = 1  # jumps per second

    # Calculate the total time of all songs in seconds
    total_time = num_songs * song_length * 60

    # Calculate the total number of jumps Lucy will make
    total_jumps = total_time * jump_rate
    result = total_jumps
    return result

print(solution())