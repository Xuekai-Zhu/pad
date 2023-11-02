def solution():
    video_length = 100
    lila_speed = 2
    num_same_videos = 6

    # Calculate Lila's total watching time
    lila_time = (video_length / (2 * lila_speed)) * num_same_videos

    # Calculate Roger's total watching time
    roger_time = (video_length / lila_speed) * num_same_videos

    # Calculate the total watching time of both Lila and Roger
    total_time = lila_time + roger_time
    result = total_time
    return result

print(solution())