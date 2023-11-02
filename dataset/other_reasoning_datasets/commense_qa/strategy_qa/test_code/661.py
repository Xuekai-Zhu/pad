def solution():
    album_name = "Meddle"
    song_name = "San Tropez"
    location_name = "French Riviera"
    if song_name in album_name and location_name in song_name:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())