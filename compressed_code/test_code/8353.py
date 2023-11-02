def solution():
    
    total_time = 180 
    talking_segments = 3
    ad_breaks = 5
    talking_time = talking_segments * 10 
    ad_break_time = ad_breaks * 5 
    total_time_spent = talking_time + ad_break_time 
    song_time = total_time - total_time_spent 
    result = song_time
    return result

print(solution())