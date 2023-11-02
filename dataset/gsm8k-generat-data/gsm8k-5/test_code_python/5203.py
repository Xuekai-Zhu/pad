def solution():
    songs = 10  # There are 10 songs in the album
    song_length = 3.5  # Each song is 3.5 minutes long
    jump_rate = 1  # Lucy can jump the rope 1 time per second

    # Calculate the total time Lucy will spend jumping rope
    total_time = songs * song_length * 60  # Convert song length to seconds

    # Calculate the total number of times Lucy will jump rope
    total_jumps = total_time * jump_rate
    result = total_jumps
    return result

print(solution())