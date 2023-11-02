def solution():
    # Calculate the total time of Gabe's playlist
    playlist_time = 3 + 2 + 3  # minutes
    # Calculate how many times Gabe can listen to his entire playlist during the 40-minute ride
    times_listening = 40 // playlist_time 
    result = times_listening
    return result

print(solution())