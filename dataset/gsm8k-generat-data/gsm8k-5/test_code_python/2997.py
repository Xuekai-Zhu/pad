def solution():
    video_length = 100  # The YouTube video is 100 hours long
    lila_speed = 2  # Lila is watching at two times the average speed
    roger_speed = 1  # Roger is watching at the average speed
    num_videos = 6  # Lila and Roger watched 6 of the same videos

    # Calculate the time Lila spent watching the video
    lila_time = video_length / lila_speed

    # Calculate the time Roger spent watching all 6 videos
    roger_time = video_length * num_videos / roger_speed

    # Calculate the total time they spent watching videos
    total_time = lila_time + roger_time
    result = total_time
    return result

print(solution())