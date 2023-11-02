def solution():
    total_videos = 411
    
    # Let's assume that Ekon watched x videos
    # Therefore, Uma watched x + 17 videos
    # And Kelsey watched x + 43 videos
    # We know that the total number of videos watched is 411
    
    x = (total_videos - 43 - 17) / 3
    
    # Kelsey watched x + 43 videos
    result = x + 43
    return result

print(solution())