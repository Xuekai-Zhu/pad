def solution():
    """Charles is jogging while listening to his favorite album. He runs at 6 MPH when he's got music on and 4 MPH when he doesn't. His album is 40 minutes long. How many minutes will it take him to jog 6 miles?"""
    # Define the jogging speeds in miles per minute
    WITH_MUSIC_SPEED = 6 / 60
    WITHOUT_MUSIC_SPEED = 4 / 60

    # Define the length of Charles's album in minutes
    ALBUM_LENGTH = 40

    # Define the jogging distance in miles
    JOGGING_DISTANCE = 6

    # Calculate the time it takes to jog 6 miles with music
    with_music_time = JOGGING_DISTANCE / WITH_MUSIC_SPEED

    # Calculate the time it takes to jog 6 miles without music
    without_music_time = JOGGING_DISTANCE / WITHOUT_MUSIC_SPEED

    # Calculate the total time including album time, taking the faster option
    if with_music_time + ALBUM_LENGTH <= without_music_time:
        total_time = with_music_time + ALBUM_LENGTH
    else:
        total_time = without_music_time + ALBUM_LENGTH

    # Convert the total time to minutes and return the result
    result = total_time * 60
    return result

print(solution())