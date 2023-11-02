def solution():
     total_storage = 16000
     used_storage = 4000
     per_song_storage = 30
     total_songs = (total_storage - used_storage) / per_song_storage
     result = total_songs
     return result

print(solution())