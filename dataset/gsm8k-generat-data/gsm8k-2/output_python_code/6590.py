def solution():
    """Gabe has three songs on his playlist. “The Best Day” is 3 minutes, “Raise the Roof” is 2 minutes, and “Rap Battle” is 3 minutes. How many times can Gabe listen to his entire playlist on the 40-minute ride to his wrestling match?"""
    total_playlist_time = 3 + 2 + 3
    rides_to_wrestling = 40 // total_playlist_time
    result = rides_to_wrestling
    return result

print(solution())