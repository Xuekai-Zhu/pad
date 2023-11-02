def solution():
    # Define the number of songs in the current album and their duration
    current_songs = 25
    current_duration = current_songs * 3

    # Define the number of songs to be added and their duration
    new_songs = 10
    new_duration = new_songs * 3

    # Calculate the total duration of the album after adding the new songs
    total_duration = current_duration + new_duration
    result = total_duration
    return result

print(solution())