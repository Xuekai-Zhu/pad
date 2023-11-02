def solution():
    """Together 3 friends watched 411 short videos. Kelsey watched 43 more than Ekon. Ekon watched 17 less than Uma. How many videos did Kelsey watch?"""
    total_videos = 411
    uma_videos = ((total_videos - 26) / 2)  # 26 is the total of the differences between Kelsey and Ekon, and Ekon and Uma
    ekon_videos = uma_videos - 17
    kelsey_videos = ekon_videos + 43
    result = kelsey_videos
    return result

print(solution())