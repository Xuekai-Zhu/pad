def solution():
    # Define the number of videos Uma watched as the reference
    uma_videos = (411 - 43 - 17) / 3

    # Calculate the number of videos Ekon watched
    ekon_videos = uma_videos - 17

    # Calculate the number of videos Kelsey watched
    kelsey_videos = ekon_videos + 43

    result = kelsey_videos
    return result

print(solution())