def solution():
    """Charles is jogging while listening to his favorite album. He runs at 6 MPH when he's got music on and 4 MPH when he doesn't. His album is 40 minutes long. How many minutes will it take him to jog 6 miles?"""
    total_distance = 6
    music_speed = 6
    no_music_speed = 4
    album_length = 40/60  # in hours
    music_distance = music_speed * album_length
    no_music_distance = total_distance - music_distance
    time_with_music = music_distance / music_speed
    time_without_music = no_music_distance / no_music_speed
    total_time = time_with_music + time_without_music
    result = total_time * 60  # in minutes
    return result

print(solution())