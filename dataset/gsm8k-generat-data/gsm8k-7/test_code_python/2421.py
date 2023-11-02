def solution():
    album_length = 40  # in minutes
    distance_covered_without_music = 4 * (album_length / 60)  # in miles
    distance_covered_with_music = 6 * (album_length / 60)  # in miles
    total_distance = 6  # in miles

    # Calculate the time taken to cover the remaining distance without music
    remaining_distance = total_distance - distance_covered_with_music
    time_without_music = (remaining_distance / 4) * 60  # in minutes

    # Calculate the total time taken
    total_time = (album_length + time_without_music)  # in minutes
    result = total_time
    return result

print(solution())