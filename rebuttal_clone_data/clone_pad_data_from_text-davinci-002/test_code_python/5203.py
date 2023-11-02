def solution():
     songs_on_album = 10
     minutes_per_song = 3.5
     seconds_per_minute = 60
     seconds_per_song = minutes_per_song * seconds_per_minute
     total_seconds = seconds_per_song * songs_on_album
     jumps_per_second = 1
     total_jumps = jumps_per_second * total_seconds
     result = total_jumps
     return result

print(solution())