def solution():
    """Rachel is an artist. She posts a speed painting video each week on her Instagram account to promote her work. To save time, she paints and records 4 videos at a time. It takes her about 1 hour to set up her painting supplies and her camera. Then she records herself painting for 1 hour per painting. She takes another 1 hour to clean up. Each video takes 1.5 hours to edit and post. How long does it take Rachel to produce a speed painting video?"""
    videos_per_session = 4
    set_up_time = 1
    painting_time = 1
    clean_up_time = 1
    editing_time = 1.5
    total_time = set_up_time + (painting_time * videos_per_session) + clean_up_time + editing_time
    result = total_time
    return result

print(solution())