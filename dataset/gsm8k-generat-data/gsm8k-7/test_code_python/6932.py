def solution():
    reading_time = 12                    # in hours
    video_game_time_per_hour = 30        # in minutes
    reward_increase_percent = 20         # percentage increase

    # Calculate the original video game time Diana would get for reading 12 hours
    original_video_game_time = reading_time * video_game_time_per_hour

    # Calculate the new reward with the 20% increase
    new_reward = reward_increase_percent / 100 + 1    # convert percent to decimal and add 1
    new_video_game_time_per_hour = video_game_time_per_hour * new_reward

    # Calculate the new total video game time Diana would get for reading 12 hours
    new_video_game_time = reading_time * new_video_game_time_per_hour

    # Calculate the difference in video game time
    additional_video_game_time = new_video_game_time - original_video_game_time

    result = additional_video_game_time
    return result

print(solution())