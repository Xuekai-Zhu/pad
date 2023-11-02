def solution():
     short_videos = 2
     long_videos = 1
     video_length_short = 2
     video_length_long = video_length_short * 6
     videos_per_week = short_videos + long_videos
     minutes_of_video = (short_videos * video_length_short) + (long_videos * video_length_long)
     result = minutes_of_video
     return result

print(solution())