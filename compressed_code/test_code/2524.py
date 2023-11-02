def solution():
    
    total_time = 3 * 60 
    talking_segments = 3 * 10 
    ad_breaks = 5 * 5 
    used_time = talking_segments + ad_breaks
    song_time = total_time - used_time
    result = song_time
    return result

print(solution())