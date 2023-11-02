def solution():
    # Calculate the total length of all the recorded videos
    total_length = 130 + 145 + 85 + 60 + 180  # in seconds

    # Convert total length to minutes
    total_length_in_minutes = total_length / 60

    # Calculate the average length of video for each player
    average_length_per_player = total_length_in_minutes / 5
    result = average_length_per_player
    return result

print(solution())