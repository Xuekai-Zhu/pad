def solution():
    """Gabe has three songs on his playlist. “The Best Day” is 3 minutes, “Raise the Roof” is 2 minutes, and “Rap Battle” is 3 minutes. How many times can Gabe listen to his entire playlist on the 40-minute ride to his wrestling match?"""
    playlist_length = 3 + 2 + 3
    ride_time = 40
    num_listens = ride_time // playlist_length
    result = num_listens
    return result

print(solution())