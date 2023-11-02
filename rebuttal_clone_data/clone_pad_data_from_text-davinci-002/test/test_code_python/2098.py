def solution():
     three_minute_songs = 10
     two_minute_songs = 15
     total_minutes = 100
     
     three_minute_songs_total_minutes = three_minute_songs * 3
     two_minute_songs_total_minutes = two_minute_songs * 2
     total_songs_minutes = three_minute_songs_total_minutes + two_minute_songs_total_minutes
     
     result = total_minutes - total_songs_minutes
     return result

print(solution())