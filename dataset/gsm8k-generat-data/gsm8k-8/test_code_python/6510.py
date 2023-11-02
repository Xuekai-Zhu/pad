def solution():
    # Calculate total time spent on one batch of 4 videos
    batch_time = 1 + (4 * 1) + 1 + (4 * 1.5)

    # Calculate time spent per video
    video_time = batch_time / 4

    result = video_time
    return result

print(solution())