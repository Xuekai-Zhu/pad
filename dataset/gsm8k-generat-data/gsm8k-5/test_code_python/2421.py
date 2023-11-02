def solution():
    album_length = 40 # Charles' album is 40 minutes long
    distance = 6 # Charles wants to jog 6 miles
    with_music = True # Charles runs at 6 MPH when he listens to music
    without_music = False # Charles runs at 4 MPH when he doesn't listen to music
    speed_with_music = 6 # Charles runs at 6 MPH when he listens to music
    speed_without_music = 4 # Charles runs at 4 MPH when he doesn't listen to music
    total_minutes = 0 # Initialize the total time

    # Calculate the time it takes to jog the distance with and without music
    time_with_music = distance / speed_with_music * 60
    time_without_music = distance / speed_without_music * 60

    # Determine how many times Charles listens to the album in the total time
    num_albums = int(total_minutes / album_length)

    # Calculate the total time it takes to jog the distance with and without music
    total_time_with_music = time_with_music + num_albums * album_length
    total_time_without_music = time_without_music + num_albums * album_length

    # Choose the faster time (with or without music)
    if total_time_with_music < total_time_without_music:
        total_minutes = total_time_with_music
    else:
        total_minutes = total_time_without_music

    result = total_minutes
    return result

print(solution())