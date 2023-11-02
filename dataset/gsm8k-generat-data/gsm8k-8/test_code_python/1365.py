def solution():
    # Calculate the total kilobytes needed for the 400 photos already on the drive
    photos_size = 400 * 1.5

    # Calculate the remaining storage space in kilobytes
    remaining_space = 2000 - photos_size

    # Calculate the size of one 200-kilobyte video in kilobytes
    video_size = 200 / 1024

    # Calculate the maximum number of 200-kilobyte videos that can fit in the remaining space
    max_videos = remaining_space // video_size

    result = int(max_videos)
    return result

print(solution())