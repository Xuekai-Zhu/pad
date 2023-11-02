def solution():
    num_videos_per_session = 4

    setup_time = 1
    painting_time = 1
    cleaning_time = 1
    editing_time = 1.5

    # Calculate the total time it takes to produce a single video
    total_time_per_video = setup_time + (num_videos_per_session * painting_time) + cleaning_time + editing_time

    result = total_time_per_video
    return result

print(solution())