def solution():
    # Calculate the distance covered while listening to music
    distance_with_music = 6 * (40/60)

    # Calculate the distance covered without music
    distance_without_music = 6 - distance_with_music

    # Calculate the time taken to cover the remaining distance
    time_taken = distance_without_music / 4

    # Calculate the total time taken
    total_time_taken = (40/60) + time_taken

    # Calculate the time taken to jog 6 miles
    time_to_jog_6_miles = (6 / 6) * total_time_taken * 60

    result = time_to_jog_6_miles
    return result

print(solution())