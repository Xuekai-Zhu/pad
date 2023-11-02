def solution():
    """Brian loves watching animal videos online.  He watches a 4-minute video of cats.  He then watches a video twice as long as the cat video involving dogs.  He finishes up his video watching for the day by watching a video on gorillas that's twice as long as the previous two videos combined.  How many minutes does Brian spend watching animal videos?"""
    # Define the length of the cat video
    cat_video = 4

    # Define the length of the dog video (twice the length of the cat video)
    dog_video = cat_video * 2

    # Define the length of the gorilla video (twice the combined length of the cat and dog videos)
    gorilla_video = (cat_video + dog_video) * 2

    # Calculate the total length of time Brian spends watching animal videos
    total_time = cat_video + dog_video + gorilla_video

    # return the result
    result = total_time
    return result

print(solution())