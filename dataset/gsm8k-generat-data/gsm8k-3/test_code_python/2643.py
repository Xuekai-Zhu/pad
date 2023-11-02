def solution():
    """Brian loves watching animal videos online.  He watches a 4-minute video of cats.  He then watches a video twice as long as the cat video involving dogs.  He finishes up his video watching for the day by watching a video on gorillas that's twice as long as the previous two videos combined.  How many minutes does Brian spend watching animal videos?"""
    # Define the length of the cat video
    cat_video_length = 4

    # Define the length of the dog video
    dog_video_length = cat_video_length * 2

    # Define the length of the gorilla video
    gorilla_video_length = (cat_video_length + dog_video_length) * 2

    # Calculate the total length of all animal videos watched
    total_video_length = cat_video_length + dog_video_length + gorilla_video_length

    # Display the total length of animal videos watched
    result = total_video_length
    return result

print(solution())