def solution():
    # Calculate the total length of Gabe's playlist
    total_playlist_length = 3 + 2 + 3

    # Calculate the number of times Gabe can listen to his entire playlist during the 40-minute ride
    num_playlist_listens = 40 // total_playlist_length

    result = num_playlist_listens
    return result

print(solution())