def solution():
    minutes_per_song = 3
    number_of_songs = 25
    minutes_to_add = 10
    total_songs = number_of_songs + minutes_to_add
    total_minutes = total_songs * minutes_per_song
    result = total_minutes
    return result

print(solution())