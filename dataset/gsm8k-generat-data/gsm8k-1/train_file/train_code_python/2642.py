def solution():
    """Brian loves watching animal videos online. He watches a 4-minute video of cats. He then watches a video twice as long as the cat video involving dogs. He finishes up his video watching for the day by watching a video on gorillas that's twice as long as the previous two videos combined. How many minutes does Brian spend watching animal videos?"""
    cat_video_duration = 4
    dog_video_duration = cat_video_duration * 2
    gorilla_video_duration = (cat_video_duration + dog_video_duration) * 2
    total_video_duration = cat_video_duration + dog_video_duration + gorilla_video_duration
    result = total_video_duration
    return result

print(solution())