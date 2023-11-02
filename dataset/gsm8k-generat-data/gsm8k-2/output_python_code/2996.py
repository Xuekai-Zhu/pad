def solution():
    """A YouTube video is 100 hours long. Lila decides to watch it at two times the average speed. Roger, her friend, also watch the same video at the average speed. If they both watched six of the same videos, what's the total number of hours they watched?"""
    video_length = 100
    lila_speed = 2
    roger_speed = 1
    same_videos = 6
    lila_time_per_video = video_length / (lila_speed * same_videos)
    roger_time_per_video = video_length / (roger_speed * same_videos)
    total_time = (lila_time_per_video + roger_time_per_video) * same_videos
    result = total_time
    return result

print(solution())