def solution():
    # Calculate the total duration of the original album
    original_duration = 25 * 3  # each song is 3 minutes long

    # Calculate the total duration of the new songs
    new_duration = 10 * 3  # each song is 3 minutes long

    # Calculate the total duration of the album after adding the new songs
    total_duration = original_duration + new_duration

    result = total_duration
    return result

print(solution())