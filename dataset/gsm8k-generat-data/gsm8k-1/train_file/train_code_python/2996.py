def solution():
    """A YouTube video is 100 hours long. Lila decides to watch it at two times the average speed. Roger, her friend, also watch the same video at the average speed. If they both watched six of the same videos, what's the total number of hours they watched?"""
    video_length = 100
    lila_speed = 2
    roger_speed = 1
    num_videos = 6
    total_hours = (video_length/lila_speed + video_length/roger_speed) * num_videos
    result = total_hours
    return result

print(solution())