def solution():
    mbps = 20
    minutes = 30
    seconds = 60
    song_size = 5
    total_mb = mbps * (minutes / seconds)
    total_songs = total_mb / song_size
    result = total_songs
    return result

print(solution())