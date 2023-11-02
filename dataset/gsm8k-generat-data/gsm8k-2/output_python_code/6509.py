def solution():
    """Rachel is an artist. She posts a speed painting video each week on her Instagram account to promote her work. To save time, she paints and records 4 videos at a time. It takes her about 1 hour to set up her painting supplies and her camera. Then she records herself painting for 1 hour per painting. She takes another 1 hour to clean up. Each video takes 1.5 hours to edit and post. How long does it take Rachel to produce a speed painting video?"""
    num_videos = 4
    setup_time = 1
    painting_time = 1
    cleanup_time = 1
    editing_time = 1.5
    total_time = (setup_time + num_videos * (painting_time + cleanup_time) + num_videos * editing_time) / num_videos
    result = total_time
    return result

print(solution())