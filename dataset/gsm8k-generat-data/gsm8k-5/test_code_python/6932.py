def solution():
    video_game_time_per_hour = 30  # Diana gets 30 minutes of video game time for every hour she reads
    dad_raise = 0.2  # Diana's dad raised her reward by 20%
    total_read_time = 12  # Diana read for 12 hours this week

    # Calculate Diana's original video game time for the week
    original_video_game_time = video_game_time_per_hour * total_read_time * 7

    # Calculate Diana's new video game time for the week after the raise
    new_video_game_time = original_video_game_time * (1 + dad_raise)

    # Calculate the difference between the two amounts of video game time
    difference = new_video_game_time - original_video_game_time

    # Convert the difference to minutes and round to the nearest whole number
    additional_video_game_time = round(difference / 60)

    result = additional_video_game_time
    return result

print(solution())