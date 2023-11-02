def solution():
    total_photo_size = 2000 * 1.5   # total size of all photos in kilobytes
    remaining_space = total_photo_size - (400 * 1.5)   # remaining space after 400 photos are stored
    video_size = 200   # size of one 200-kilobyte video

    # Calculate the maximum number of 200-kilobyte videos that can be stored on the remaining space
    num_videos = remaining_space // video_size
    result = num_videos
    return result

print(solution())