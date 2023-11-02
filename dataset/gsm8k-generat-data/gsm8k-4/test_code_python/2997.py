def solution():
    """A YouTube video is 100 hours long. Lila decides to watch it at two times the average speed. Roger, her friend, also watch the same video at the average speed. If they both watched six of the same videos, what's the total number of hours they watched?"""
    # Define the length of the video and the number of videos watched
    VIDEO_LENGTH = 100
    NUM_VIDEOS = 6

    # Calculate Lila's total watching time
    lila_time = (VIDEO_LENGTH * NUM_VIDEOS) / 2

    # Calculate Roger's total watching time
    roger_time = VIDEO_LENGTH * NUM_VIDEOS

    # Calculate the total time watched by both Lila and Roger
    total_time = lila_time + roger_time

    result = total_time
    return result

print(solution())