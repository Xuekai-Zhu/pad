def solution():
    """A YouTube video is 100 hours long. Lila decides to watch it at two times the average speed. Roger, her friend, also watch the same video at the average speed. If they both watched six of the same videos, what's the total number of hours they watched?"""
    # Define the length of the YouTube video in hours
    video_length = 100

    # Calculate Lila's total time to watch one video at double speed
    lila_speed = 2
    lila_time = video_length / lila_speed

    # Calculate Roger's total time to watch one video at average speed
    roger_speed = 1
    roger_time = video_length / roger_speed

    # Calculate the total time they watched for six videos
    total_time = (lila_time + roger_time) * 6

    # Display the total time they watched
    result = total_time
    return result

print(solution())