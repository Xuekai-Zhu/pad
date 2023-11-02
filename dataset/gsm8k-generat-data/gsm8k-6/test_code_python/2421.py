def solution():
    album_length = 40  # length of Charles' favorite album in minutes
    distance_covered_with_music = 6 * (album_length / 60)  # distance covered in 40 minutes when running at 6 mph
    distance_covered_without_music = 6 - distance_covered_with_music  # distance left to cover at 4 mph
    time_taken_without_music = distance_covered_without_music / 4  # time taken to cover remaining distance at 4 mph
    total_time_taken = (album_length + (time_taken_without_music * 60))  # total time taken to jog 6 miles
    result = total_time_taken
    return result

print(solution())