def solution():
    mph_with_music = 6
    mph_without_music = 4
    minutes_in_album = 40
    total_miles = minutes_in_album / mph_with_music
    result = minutes_in_album / mph_without_music
    return result

print(solution())