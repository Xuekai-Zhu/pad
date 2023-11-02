def solution():
    """Charles is jogging while listening to his favorite album. He runs at 6 MPH when he's got music on and 4 MPH when he doesn't. His album is 40 minutes long. How many minutes will it take him to jog 6 miles?"""
    # Define the running speeds
    MUSIC_SPEED = 6
    NO_MUSIC_SPEED = 4

    # Define the album length
    ALBUM_LENGTH = 40 # in minutes

    # Define the jogging distance
    DISTANCE = 6 # in miles

    # Calculate the time taken to jog with music
    time_with_music = DISTANCE / MUSIC_SPEED # in hours
    time_with_music *= 60 # convert to minutes

    # Calculate the time taken to jog without music
    time_without_music = (ALBUM_LENGTH / 60) - (DISTANCE / MUSIC_SPEED) # in hours
    time_without_music *= 60 # convert to minutes
    time_without_music += DISTANCE / NO_MUSIC_SPEED * 60 # add time taken to jog without music

    # Calculate the total time taken
    total_time = time_with_music + time_without_music

    # Display the total time taken
    result = total_time
    return result

print(solution())