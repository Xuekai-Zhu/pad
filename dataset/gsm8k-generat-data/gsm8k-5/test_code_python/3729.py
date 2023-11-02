def solution():
    minutes_in_run = 100
    total_minutes_on_playlist = (10 * 3) + (15 * 2)  # Total minutes of songs on the playlist

    # Calculate how many more minutes of songs Stan needs in his playlist to cover his entire run
    minutes_left = minutes_in_run - total_minutes_on_playlist
    result = minutes_left
    return result

print(solution())