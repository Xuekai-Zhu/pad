def solution():
    cat_video_length = 4  # Brian watches a 4-minute video of cats
    dog_video_length = cat_video_length * 2  # Brian watches a video twice as long as the cat video involving dogs
    gorilla_video_length = (cat_video_length + dog_video_length) * 2  # Brian watches a video on gorillas that's twice as long as the previous two videos combined

    # Calculate the total time Brian spent watching animal videos
    total_time = cat_video_length + dog_video_length + gorilla_video_length
    result = total_time
    return result

print(solution())