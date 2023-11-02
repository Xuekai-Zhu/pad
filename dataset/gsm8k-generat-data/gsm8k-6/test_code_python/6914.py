def solution():
    # Calculate the total number of videos Billy watches
    total_videos = 15 * 5  # Billy watches 15 videos each time he generates suggestions, and he does this 5 times
    total_rejections = 5  # Billy rejects 5 sets of suggestions before finding a video to watch
    watched_videos = total_videos - total_rejections  # Billy watches all videos except for the 5 he rejects
    desired_video_number = 5  # Billy picks the 5th show on the final suggestion list
    result = watched_videos + desired_video_number
    return result

print(solution())