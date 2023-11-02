def solution():
    """Charles is jogging while listening to his favorite album. He runs at 6 MPH when he's got music on and 4 MPH when he doesn't. His album is 40 minutes long. How many minutes will it take him to jog 6 miles?"""
    music_speed = 6 # in miles per hour
    non_music_speed = 4 # in miles per hour
    album_length = 40 # in minutes
    album_length_hours = album_length / 60 # convert to hours
    distance = 6 # in miles
    
    time_with_music = distance / music_speed # in hours
    time_without_music = distance / non_music_speed # in hours
    
    total_time = (time_with_music * album_length_hours) + (time_without_music * (1 - album_length_hours)) # weighted average based on album length
    
    # convert total time to minutes
    result = total_time * 60 
    
    return result

print(solution())