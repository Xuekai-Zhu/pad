def solution():
    """Brian loves watching animal videos online. He watches a 4-minute video of cats. He then watches a video twice as long as the cat video involving dogs. He finishes up his video watching for the day by watching a video on gorillas that's twice as long as the previous two videos combined. How many minutes does Brian spend watching animal videos?"""
    cat_video_time = 4
    dog_video_time = cat_video_time * 2
    gorilla_video_time = (cat_video_time + dog_video_time) * 2
    total_time = cat_video_time + dog_video_time + gorilla_video_time
    result = total_time
    return result

print(solution())