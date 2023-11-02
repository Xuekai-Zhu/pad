def solution():
    """Diana gets 30 minutes of video game time for every hour she reads. Her dad decided to raise her reward by 20%. Diana read for 12 hours this week. How many more minutes of video game time will she get as a result of her raise?"""
    # Define the original video game time per hour of reading and the percentage increase
    ORIGINAL_TIME_PER_HOUR = 30
    PERCENT_INCREASE = 20

    # Define the number of hours Diana read this week
    hours_read = 12

    # Calculate Diana's original total video game time
    original_video_game_time = ORIGINAL_TIME_PER_HOUR * hours_read * 2

    # Calculate Diana's new video game time with the percentage increase
    new_time_per_hour = ORIGINAL_TIME_PER_HOUR * (100 + PERCENT_INCREASE) / 100
    new_video_game_time = new_time_per_hour * hours_read * 2

    # Calculate the difference in video game time between the original and new rewards
    additional_video_game_time = new_video_game_time - original_video_game_time

    # Display the additional video game time Diana receives due to the raise
    result = additional_video_game_time
    return result

print(solution())