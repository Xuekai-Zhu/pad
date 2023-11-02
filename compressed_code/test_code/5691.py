def solution():
    
    total_time = 60
    added_time = 16 * 3
    remaining_time = total_time - added_time
    songs_needed = remaining_time // 4
    result = songs_needed
    return result

print(solution())