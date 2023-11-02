def solution():
    """Together 3 friends watched 411 short videos. Kelsey watched 43 more than Ekon. Ekon watched 17 less than Uma. How many videos did Kelsey watch?"""
    # Define the total number of videos watched
    total_videos = 411

    # Calculate the number of videos watched by Uma
    uma_videos = (total_videos - 43 + 17) / 3

    # Calculate the number of videos watched by Ekon
    ekon_videos = uma_videos - 17

    # Calculate the number of videos watched by Kelsey
    kelsey_videos = ekon_videos + 43

    # return the result
    result = kelsey_videos
    return result

print(solution())