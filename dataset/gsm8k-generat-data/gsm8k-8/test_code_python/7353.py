def solution():
    # Convert the total concert time to minutes
    total_time = 80

    # Subtract the intermission time from the total time
    concert_time = total_time - 10

    # Divide the remaining time by the length of a regular song to get the number of regular songs
    regular_songs = concert_time // 5

    # Subtract the time of the longer song from the remaining time
    remaining_time = concert_time - (regular_songs * 5)

    # If there's still time left over, there was an extra song
    if remaining_time >= 10:
        num_songs = regular_songs + 2
    else:
        num_songs = regular_songs + 1

    result = num_songs
    return result

print(solution())