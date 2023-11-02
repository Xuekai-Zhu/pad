def solution():
    # Define the host of Dancing with the Stars and the host of America's Funniest Home Videos
    dancing_host = "Tom Bergeron"
    funniest_videos_host = "Tom Bergeron"
    # Check if Tom Bergeron is hosting two different shows at the same time
    if dancing_host != funniest_videos_host:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())